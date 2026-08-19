# Question Bank Generation Guide — Data Mining TP Evaluation

## Goal

Generate **1000 True/False questions** across **6 TPs**, from the provided
LaTeX TP and course files, split into **three categories**:

- **350 plain standalone questions** — straightforward, no deliberate
  misdirection.
- **150 trick standalone questions** — a single statement, not paired with
  anything, that *sounds* correct (uses the right vocabulary, mimics the
  phrasing of a true fact, invokes a common misconception) but is actually
  **False** (or, more rarely, sounds obviously wrong but is actually
  **True**). Unlike trap pairs, there's no sibling question — the trickiness
  is self-contained in the wording alone.
- **500 trap questions organized as 250 pairs** — two near-identical
  statements per pair, differing in exactly one detail, with **opposite**
  `correct_answer` (see §Trap pair guidelines below).

Target roughly **166–167 total questions per TP** (~58 plain + ~25 trick +
~83–84 trap-paired), adjusted to how much material each TP actually covers —
do not force uniform counts if one TP has thin content; flag it instead of
padding with trivial questions.

---

## Input material

For each TP, use:
- The TP's own LaTeX source (instructions, exercises, expected outputs).
- The corresponding course LaTeX source (definitions, theorems, algorithm
  descriptions, formulas) for the same topic.

Questions must be answerable from this material alone — no outside
knowledge required, no ambiguity that depends on an edition-specific
textbook definition not present in the given files.

---

## Output format

Produce one CSV (or JSON, whichever is easier to import into Postgres) per
TP, matching the `questions` table columns:

```csv
tp_id,topic_id,text,correct_answer,question_type,trap_group_id,trap_mode
1,3,"Text of a plain standalone statement.",true,plain,,
1,3,"Text of a trick standalone statement that sounds right but isn't.",false,trick,,
1,3,"Text of statement A of pair 12.",true,trap,12,hidden
1,3,"Text of statement B of pair 12.",false,trap,12,hidden
```

- `question_type`: one of `plain`, `trick`, `trap` — this is a generation
  convenience for you and for reviewers; if you'd rather not add a new DB
  column, it can be dropped before import since `trap_group_id` already
  distinguishes trap questions, and `trick` questions can simply be
  standalone rows (null `trap_group_id`) — just keep the label in your own
  working file so trick questions get the extra scrutiny pass described
  below.
- `trap_group_id`: shared integer for the two questions in a pair, unique
  per pair, null for standalone (plain or trick) questions.
- `trap_mode`: `hidden` (never shown together in one attempt — tests
  whether the student truly knows the fact vs. pattern-matching) or
  `attention_check` (may be shown together, deliberately — catches
  skimming/bots by checking for self-contradiction). Aim for roughly
  **70% hidden / 30% attention_check** among the trap pairs — attention
  pairs are a deliberate detection tool, not the primary difficulty
  mechanism, so most traps should test real understanding.

---

## Standalone question guidelines (the 500)

- One factual/conceptual claim per question, unambiguously True or False
  from the source material.
- Roughly balance True vs. False across the full bank (avoid a pattern like
  "True is always the safe guess") — aim for 45–55% split per TP, not
  exactly 50/50 (an exact split is itself a detectable pattern).
- Mix question types:
  - Definition checks ("X is defined as...")
  - Algorithm/procedure checks ("Step N of algorithm X does...")
  - Property/theorem checks ("X always converges when...")
  - Numeric/formula checks ("The complexity of X is O(...)")
  - TP-specific checks (expected output/behavior of a specific exercise)
- Avoid: double negatives, "always/never" absolutism unless the source
  material itself states an absolute, and questions answerable by
  test-taking strategy alone (e.g. oddly specific numbers that are obviously
  the odd one out).
- Keep each statement short enough to read and decide within the 20s
  window — one clause, not a paragraph.

---

## Trick question guidelines (the 150 standalone trick questions)

These differ from trap pairs in one key way: **there is no sibling
question** — the misdirection has to live entirely inside a single sentence.
The goal is a statement a student who skims or half-remembers the material
would confidently mark correctly, but a student who actually understood it
would catch.

Good sources of trick questions from course/TP material:
- **Common misconceptions**: if the course explicitly corrects a
  misunderstanding ("students often think X, but actually Y"), that
  correction is prime trick-question material — state the misconception as
  if it were fact.
- **Plausible-sounding but reversed causality** ("X happens because of Y"
  when actually Y happens because of X).
- **Overgeneralization of a rule that has an exception** stated in the
  material (a property that holds "in most cases" or "under condition Z",
  presented as if it held unconditionally).
- **Correct terminology, wrong definition** — using the right technical word
  but attaching a definition that belongs to a different, related concept
  from the same TP (e.g. two metrics or two algorithms that are commonly
  confused).
- **Off-by-one / near-miss numeric claims** that are close enough to the
  real value or formula to look right at a glance (e.g. a complexity class
  one step off, a formula missing one term).
- Occasionally invert the pattern: a statement that *sounds* wrong (unusual
  phrasing, counterintuitive claim) but is actually **True** according to
  the source — this stops "sounds suspicious → mark False" from becoming a
  winning heuristic on its own.

Rules:
- One sentence, no compound claims (a compound claim risks being "half
  right, half wrong," which is genuinely ambiguous rather than tricky).
- The misleading element must be traceable to something *actually present*
  in the course/TP material (a real misconception the material addresses, a
  real related-but-different concept) — never invent a plausible-sounding
  fabrication with no basis in the source, since that risks teaching a false
  association even in the act of testing.
- Verify every trick question's `correct_answer` against the source with
  extra care — an incorrectly-keyed trick question is the worst case in the
  whole bank, since it looks deliberately designed to penalize the students
  who understood the material best.

---

## Trap pair guidelines (the 250 pairs / 500 questions)

This is the core "concentration" mechanism requested. Each pair should
differ by exactly **one** changed element that flips the truth value:

Examples of the kind of single-element flip to construct (write your own
from the actual course/TP content, these just show the *pattern*):
- A numeric parameter changed (e.g. a stated complexity, threshold, or
  count) while the surrounding sentence is identical.
- A direction/comparison reversed (increases → decreases, minimum →
  maximum, before → after).
- A named entity swapped for a similar but distinct one from the same TP
  (e.g. two different algorithms, two different metrics).
- A condition's scope changed (always → only when X, all → some).
- A step order swapped in a described procedure.

Rules:
- The two statements in a pair must be genuinely close in wording — that's
  what makes them require concentration rather than simple recall.
- Do not make the flipped element the most salient word in the sentence
  (e.g. don't just bold-worthy capitalize the changed term); it should
  require actually reading the whole statement.
- Verify both members of every pair against the source material yourself —
  a trap pair with a wrong `correct_answer` is worse than a normal wrong
  question, since it actively penalizes students who understood the
  material correctly.

---

## Per-question metadata checklist (do this for every generated question)

- [ ] Traceable to a specific passage in the given TP/course LaTeX (keep an
      internal mapping while generating, even if not stored in the DB, so
      disputed questions can be checked later).
- [ ] Unambiguous — no reasonable reading gives the opposite answer.
- [ ] Under ~25 words where possible (readable well inside 20s).
- [ ] Assigned to the correct `topic_id` within its TP.
- [ ] For trap pairs: both members checked against source, `trap_group_id`
      matches, `trap_mode` assigned deliberately (not randomly).
- [ ] For trick questions: the misleading element is traceable to a real
      misconception or a real related concept in the source material, not
      invented from scratch.

---

## Suggested generation workflow

1. For each TP, extract a list of atomic facts/claims from the LaTeX
   (definitions, algorithm steps, stated properties, TP-specific expected
   behaviors) — this becomes your source list before writing any question.
   While doing this, separately note any misconceptions the course material
   explicitly flags, and any pairs of similar-but-distinct concepts — these
   feed directly into trick questions and trap pairs.
2. From that list, write plain standalone questions first (~58 per TP),
   covering the list broadly rather than clustering on a few easy facts.
3. From the noted misconceptions/near-confusions, write trick standalone
   questions (~25 per TP).
4. From the same source list, identify ~83–84 facts per TP that have a
   natural "close but wrong" variant, and write the trap pairs.
5. Do a pass balancing True/False ratio per TP, across all three
   categories combined.
6. Do a final verification pass re-reading each question against the
   source material before exporting — treat trick questions and trap pairs
   with extra scrutiny since a mis-keyed answer there is more damaging than
   in a plain question.

---

## Bank rotation note

Keep the mapping from question → source passage and generation batch/date
even after questions go live. This makes it easy to retire and replace
~10–15% of the bank each semester (per the anti-harvesting measure in
APP_SPEC.md §6) without having to regenerate everything from scratch.