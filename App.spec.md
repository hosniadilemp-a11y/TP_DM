# TP Continuous Evaluation App — Build Specification

## 1. Purpose

A web app for timed True/False quizzes used as continuous evaluation on 6 Data
Mining TPs (practical works). Students identify themselves with a structured
code only (e.g. `IASD01`), no personal data is stored. Every design decision
below prioritizes **server-side authority** — the frontend must never receive
a correct answer, a full question bank, or more than one question at a time.

Stack: **FastAPI (Python) backend + Postgres (Supabase) + static frontend**,
deployed on **Render** (backend + static site) with **Supabase** as the
database only. The frontend must NEVER call Supabase directly — only the
backend holds the Supabase service-role key.

---

## 2. Locked decisions

- Attempt length: **20 questions per attempt**, randomly sampled.
- Multiple attempts allowed per (code, TP) across the whole TP period.
- Cooldown: **10 minutes** between two attempts of the *same* (code, TP).
  (Open: whether cooldown is per-TP or global per code — default to
  **per (code, TP)** unless told otherwise; a student may start a different
  TP immediately.)
- Timer: **20 seconds per question**, enforced **server-side only**.
- Question bank: **1000 questions total** = **350 plain standalone + 150
  trick standalone + 500 trap questions organized in 250 trap pairs** (see
  QUESTION_GENERATION.md).
- **Scoring**: +1 point for a correct answer, **−1 point for a wrong or late
  answer**, 0 for an unanswered/skipped question if that state is ever
  possible. This penalizes blind 50/50 guessing (expected value of random
  guessing ≈ 0), unlike simple %-correct scoring.
  - Raw score per attempt ranges from **−20 to +20** (20 questions).
  - Normalize to the **0–20 scale** used for the test mark:
    `final_mark = 10 + raw_score / 2`
    - All correct (raw +20) → 20/20.
    - All wrong (raw −20) → 0/20.
    - Pure random guessing (raw ≈ 0 in expectation) → **10/20** — this
      lands exactly on the standard French passing threshold, which is a
      convenient, intentional side effect of this formula: a student who
      genuinely knows nothing and guesses blindly should expect to sit right
      at the pass/fail line, not comfortably above it.
  - Store `raw_score` (integer, −20..20) on `attempts.score` and compute
    `final_mark` at read time (in the analysis script) rather than storing a
    second column — keeps the DB as the single source of truth for the raw
    count.
- Scoring shown to student: **final mark only** (the 0–20 number), never
  per-question feedback, never the correct answer.
- One question served at a time; the next is not issued until the current one
  is answered or has expired.
- Semester analysis: per (code, TP), take **all attempts' `raw_score`**,
  apply **IQR outlier trimming** (Q1 − 1.5·IQR to Q3 + 1.5·IQR), average the
  rest, then convert the trimmed average to a mark with
  `10 + avg_raw_score / 2`. If a student has fewer than 4 attempts for a TP,
  skip IQR (not enough points to define quartiles) and use the plain median
  of `raw_score` instead, converted the same way. Final grade per student =
  average of the 6 per-TP marks (each already on the 0–20 scale).

---

## 3. Database schema (Postgres / Supabase)

```sql
-- Valid student identifiers, seeded once per semester/promotion
CREATE TABLE valid_codes (
  code TEXT PRIMARY KEY,          -- e.g. 'IASD01'
  group_code TEXT NOT NULL,       -- e.g. 'IASD'
  active BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE tp (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  ordering INT NOT NULL
);

CREATE TABLE topics (
  id SERIAL PRIMARY KEY,
  tp_id INT REFERENCES tp(id),
  name TEXT NOT NULL
);

CREATE TABLE questions (
  id SERIAL PRIMARY KEY,
  tp_id INT REFERENCES tp(id),
  topic_id INT REFERENCES topics(id),
  text TEXT NOT NULL,
  correct_answer BOOLEAN NOT NULL,
  trap_group_id INT NULL,         -- links paired trap questions together
  trap_mode TEXT NULL CHECK (trap_mode IN ('hidden','attention_check')),
  active BOOLEAN NOT NULL DEFAULT TRUE,
  retired_at TIMESTAMP NULL
);

CREATE TABLE sessions (
  id SERIAL PRIMARY KEY,
  tp_id INT REFERENCES tp(id),
  opens_at TIMESTAMP NOT NULL,
  closes_at TIMESTAMP NOT NULL
);

CREATE TABLE attempts (
  id SERIAL PRIMARY KEY,
  code TEXT REFERENCES valid_codes(code),
  tp_id INT REFERENCES tp(id),
  session_id INT REFERENCES sessions(id),
  started_at TIMESTAMP NOT NULL DEFAULT now(),
  ended_at TIMESTAMP NULL,
  status TEXT NOT NULL DEFAULT 'in_progress'
    CHECK (status IN ('in_progress','finished','abandoned')),
  score NUMERIC NULL,
  device_fingerprint TEXT NULL,
  ip_hash TEXT NULL,
  user_agent TEXT NULL,
  flagged BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE attempt_answers (
  id SERIAL PRIMARY KEY,
  attempt_id INT REFERENCES attempts(id),
  question_id INT REFERENCES questions(id),
  position INT NOT NULL,          -- 1..20, order served
  shown_at TIMESTAMP NOT NULL,    -- server clock, set when question dispatched
  answered_at TIMESTAMP NULL,     -- server clock, set on submission
  chosen BOOLEAN NULL,
  is_correct BOOLEAN NULL,
  response_ms INT NULL,
  is_late BOOLEAN NOT NULL DEFAULT FALSE
);
```

Row Level Security: enable RLS on every table and grant **no** access to the
`anon` key. Only the backend's service-role key touches the database. If RLS
is not configured this way, a student can query Supabase's auto-REST API
directly and pull `correct_answer` for the whole bank — this is the single
most important security rule in this spec.

---

## 4. API endpoints (backend only, frontend talks to nothing else)

### `POST /attempt/start`
Body: `{ code, tp_id }`
- Validate `code` exists in `valid_codes` AND is `active` (generic error
  message on failure — do not reveal whether the prefix or number was wrong).
- Validate current server time falls within an open `sessions` row for
  `tp_id` (session-gating — reject outside the window regardless of URL
  access).
- Enforce 10-minute cooldown: reject if `now - last attempt.ended_at < 10 min`
  for this `(code, tp_id)`.
- Enforce a daily/attempt rate cap per code (see §6, harvesting defense).
- Collect device fingerprint from client-provided signals (user agent, screen
  resolution, timezone offset) + hashed IP, store on the `attempts` row.
- Create `attempts` row, status `in_progress`.
- Return `attempt_id` only. No questions yet.

### `GET /attempt/{id}/next-question`
- Confirm attempt belongs to caller and is `in_progress`.
- If the previous question (if any) has no `answered_at` and its 20s+buffer
  has expired, mark it `is_late = true`, `is_correct = false` first.
- Stop and finalize (see `/finish`) once 20 questions have been served.
- Pick next question: randomly sampled from `questions` where `tp_id`
  matches and `active = true`, not already served in this attempt, respecting
  trap-pair rules (see QUESTION_GENERATION.md — `hidden` pairs never both
  appear in the same attempt; `attention_check` pairs may both appear but
  separated by several other questions).
- Insert `attempt_answers` row with `shown_at = now()`, `chosen = NULL`.
- Return **only** `{ question_id, text, options: [true,false] }`. Never
  include `correct_answer`.

### `POST /attempt/{id}/answer`
Body: `{ question_id, chosen }`
- Look up the matching `attempt_answers` row by `attempt_id + question_id`.
- Compute `response_ms = now() - shown_at` (server clock only — ignore any
  client-reported timing).
- If `response_ms > 20000 + LATENCY_BUFFER_MS` (buffer ≈ 1500–2000ms), mark
  `is_late = true`, `is_correct = false`, ignore `chosen` for correctness
  (still store it for analysis).
- Otherwise grade against `questions.correct_answer`, store `is_correct`.
- Return **no feedback** — just `{ "received": true }`. Never echo back
  whether the answer was right.

### `POST /attempt/{id}/finish`
- Mark any still-unanswered question as late/incorrect.
- Compute `raw_score = correct_count - wrong_or_late_count` (range −20..20).
- Compute `final_mark = 10 + raw_score / 2` (range 0..20).
- Store `raw_score` in `attempts.score`, set `ended_at = now()`,
  `status = 'finished'`.
- Return `{ final_mark }` only — not the raw correct/wrong breakdown, to
  avoid letting a student back-derive which questions they got wrong.

---

## 5. Frontend requirements

- Static SPA (plain HTML/JS or a lightweight framework — keep it simple,
  no build-heavy stack needed).
- Talks only to the backend's REST API, never to Supabase.
- Displays one question at a time with a visible 20s countdown for UX, but
  this client countdown is cosmetic only — the server is the enforcement
  authority. Client expiry should still auto-submit `chosen = null` (or
  disable input) so the UI doesn't feel broken even though the server
  independently enforces the deadline.
- No dev-tools-visible payload should ever contain a correct answer or
  future questions — verify this by inspecting actual Network tab responses
  during testing, not just by reading the code.
- Shows only: current question number (e.g. "7 / 20"), the question,
  True/False buttons, countdown. At the end: final score only.

---

## 6. Anti-cheating measures to implement (see also QUESTION_GENERATION.md §trap questions)

1. **No answer in any HTTP response** — grading is 100% server-side.
2. **One question at a time**, server refuses to serve question *n+1* before
   *n* is answered/expired (blocks bulk-harvesting the bank via the API).
3. **Server-side timer** using `shown_at`/`answered_at` timestamps from the
   DB row, never trusting client-submitted timing.
4. **Rate limiting**: cap total questions servable per `code` per day (e.g.
   ~120–150, enough for ~6 legitimate attempts, well below what's needed to
   harvest all 1000 questions one at a time).
5. **10-minute cooldown** between attempts of the same (code, TP), enforced
   against `attempts.ended_at`, not inferable from client state.
6. **Device fingerprint + hashed IP** stored per attempt. Run a periodic
   (e.g. nightly) report flagging: (a) one fingerprint used across many
   different codes in the same session window (proxy test-taker pattern);
   (b) codes whose fingerprint changes attempt-to-attempt AND also appears
   under other codes (combine both signals — a changing fingerprint alone is
   normal, e.g. different lab computers).
7. **Response-time + accuracy anomaly report** (batch, not live-blocking):
   flag attempts with high accuracy (>90%) and unusually fast, low-variance
   response times — signature of a scripted/LLM-in-the-loop bot answering via
   direct API calls rather than a human reading each question. This is
   advisory for manual review, not an automatic penalty (false positives from
   genuinely fast, well-prepared students are expected).
8. **Attention-check trap pairs**: flag attempts where a student answers both
   members of an `attention_check` pair identically despite opposite correct
   answers — a self-contradiction signal independent of raw score.
9. **Session-gating**: `/attempt/start` only succeeds inside an open
   `sessions` window for that TP — the app is functionally inert outside
   class time regardless of whether someone finds the URL.
10. **Bank rotation**: plan to retire/replace ~10–15% of questions each
    semester so a previously leaked answer key partially depreciates.

---

## 7. Deployment

- **Supabase**: Postgres database only. Enable RLS on all tables, no
  `anon`/public access. Store the service-role key as a Render environment
  variable, never in frontend code or a public repo.
- **Render**: one Web Service for the FastAPI backend (holds the Supabase
  service-role key as an env var), one Static Site for the frontend (env var
  pointing to the backend's public URL, nothing else).
- Do not commit `.env` files; use Render's environment variable dashboard.

---

## 8. Suggested build order

1. Schema + seed `tp`, `topics`, `valid_codes` (from the real student list),
   one `sessions` row for testing.
2. `/attempt/start`, `/attempt/{id}/next-question`, `/attempt/{id}/answer`,
   `/attempt/{id}/finish` — test with `curl`/Postman before touching the UI.
3. Minimal frontend: code entry → one question at a time → final score.
4. Add device fingerprinting + rate limiting + cooldown enforcement.
5. Load the real question bank (see QUESTION_GENERATION.md).
6. Build the end-of-semester analysis script (IQR-per-student-per-TP, as
   described in §2) as a separate offline script reading directly from
   Supabase with the service-role key — this does not need to be part of the
   web app itself.