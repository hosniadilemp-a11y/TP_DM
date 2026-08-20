import os
import json
import hashlib
import random
from datetime import datetime, timedelta
from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session as DBSession
from sqlalchemy import func, or_

from student_app.app.database import get_db
from student_app.app.models import ValidCode, TP, Question, Session, Attempt, AttemptAnswer
from student_app.app.schemas import (
    TPInfo,
    AttemptStartRequest,
    AttemptStartResponse,
    QuestionServeResponse,
    AnswerSubmitRequest,
    AnswerSubmitResponse,
    FinishAttemptResponse,
    ViolationEventRequest,
    ViolationEventResponse
)

router = APIRouter(prefix="/api", tags=["attempts"])

LATENCY_BUFFER_MS = 2000  # 2 seconds server clock tolerance
QUESTION_TIMEOUT_SEC = 20
COOLDOWN_MINUTES = 10
MAX_DAILY_ATTEMPTS = int(os.getenv("MAX_DAILY_ATTEMPTS", 50))  # 50 per day for dev testing

def get_client_ip(request: Request) -> str:
    if not request:
        return "127.0.0.1"
    forwarded_for = request.headers.get("x-forwarded-for")
    if forwarded_for:
        return forwarded_for.split(",")[0].strip()
    return request.client.host if request.client else "127.0.0.1"

@router.get("/tps", response_model=List[TPInfo])
def get_tps(db: DBSession = Depends(get_db)):
    tps = db.query(TP).order_by(TP.ordering).all()
    return tps

@router.post("/attempt/start", response_model=AttemptStartResponse)
def start_attempt(
    req_data: AttemptStartRequest,
    request: Request,
    db: DBSession = Depends(get_db)
):
    clean_code = req_data.code.strip().upper()

    # 1. Validate Code
    student = db.query(ValidCode).filter(ValidCode.code == clean_code, ValidCode.active == True).first()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Wrong student code typed: '{clean_code}'. Please check your speciality prefix (SIAD, IASD, RSD, CS) and number (01..100)."
        )

    # 2. Check Session Gating
    now = datetime.utcnow()
    active_session = db.query(Session).filter(
        Session.tp_id == req_data.tp_id,
        Session.opens_at <= now,
        Session.closes_at >= now
    ).first()

    if not active_session:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"No active evaluation session open for TP {req_data.tp_id}."
        )

    # 3. Enforce 10-minute Cooldown per (code, tp_id)
    cooldown_cutoff = now - timedelta(minutes=COOLDOWN_MINUTES)

    # Check if an active attempt is currently in_progress -> RESUME IT!
    in_progress_attempt = db.query(Attempt).filter(
        Attempt.code == clean_code,
        Attempt.tp_id == req_data.tp_id,
        Attempt.status == "in_progress"
    ).order_by(Attempt.started_at.desc()).first()

    if in_progress_attempt:
        return {"attempt_id": in_progress_attempt.id}

    # Check cooldown against finished attempts within 10 minutes by IP, Device Fingerprint, or Code
    client_ip = get_client_ip(request)
    fp = req_data.device_fingerprint

    cooldown_filters = [Attempt.code == clean_code]
    if client_ip:
        cooldown_filters.append(Attempt.client_ip == client_ip)
    if fp:
        cooldown_filters.append((Attempt.device_fingerprint == fp) & (Attempt.device_fingerprint != None) & (Attempt.device_fingerprint != ""))

    recent_finished = db.query(Attempt).filter(
        Attempt.status == "finished",
        Attempt.ended_at >= cooldown_cutoff,
        or_(*cooldown_filters)
    ).order_by(Attempt.ended_at.desc()).first()

    if recent_finished:
        time_elapsed = (now - recent_finished.ended_at).total_seconds()
        remaining_sec = int((COOLDOWN_MINUTES * 60) - time_elapsed)
        if remaining_sec > 0:
            remaining_min = max(1, (remaining_sec + 59) // 60)
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail=f"Cooldown active (TP {recent_finished.tp_id} completed). Please wait {remaining_min} minute(s) before starting any attempt. ({remaining_sec}s remaining)",
                headers={"X-Cooldown-Remaining-Sec": str(remaining_sec)}
            )

    # 4. Enforce Daily Attempt Cap per code
    start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0)
    today_attempts_count = db.query(Attempt).filter(
        Attempt.code == clean_code,
        Attempt.started_at >= start_of_day
    ).count()

    if today_attempts_count >= MAX_DAILY_ATTEMPTS:
        raise HTTPException(
            status_code=status.HTTP_429_TOO_MANY_REQUESTS,
            detail=f"Daily attempt limit reached (maximum {MAX_DAILY_ATTEMPTS} attempts per day)."
        )

    # 5. Device fingerprinting + IP Hash
    forwarded_for = request.headers.get("x-forwarded-for")
    if forwarded_for:
        raw_ip = forwarded_for.split(",")[0].strip()
    else:
        raw_ip = request.client.host if request.client else "127.0.0.1"

    ip_hash = hashlib.sha256(raw_ip.encode("utf-8")).hexdigest()[:16]
    user_agent = req_data.user_agent or request.headers.get("user-agent", "Unknown")

    attempt = Attempt(
        code=clean_code,
        tp_id=req_data.tp_id,
        session_id=active_session.id,
        started_at=now,
        status="in_progress",
        device_fingerprint=req_data.device_fingerprint,
        client_ip=raw_ip,
        ip_hash=ip_hash,
        user_agent=user_agent
    )
    db.add(attempt)
    db.commit()
    db.refresh(attempt)

    return {"attempt_id": attempt.id}

_QUESTIONS_CACHE = {}

def _get_tp_questions_dict(db: DBSession, tp_id: int):
    global _QUESTIONS_CACHE
    if tp_id not in _QUESTIONS_CACHE:
        raw_qs = db.query(Question).filter(
            Question.tp_id == tp_id,
            Question.active == True
        ).all()
        _QUESTIONS_CACHE[tp_id] = [
            {
                "id": q.id,
                "text": q.text,
                "correct_answer": q.correct_answer,
                "trap_group_id": q.trap_group_id,
                "trap_mode": q.trap_mode
            }
            for q in raw_qs
        ]
    return _QUESTIONS_CACHE[tp_id]

@router.get("/attempt/{attempt_id}/next-question")
def get_next_question(attempt_id: int, db: DBSession = Depends(get_db)):
    attempt = db.query(Attempt).filter(Attempt.id == attempt_id).first()
    if not attempt:
        raise HTTPException(status_code=404, detail="Attempt not found.")

    if attempt.status != "in_progress":
        raise HTTPException(status_code=400, detail="Attempt is already finished or abandoned.")

    now = datetime.utcnow()

    served_answers = db.query(AttemptAnswer).filter(
        AttemptAnswer.attempt_id == attempt_id
    ).order_by(AttemptAnswer.position).all()

    if served_answers:
        last_answer = served_answers[-1]
        if last_answer.answered_at is None:
            elapsed_ms = (now - last_answer.shown_at).total_seconds() * 1000
            if elapsed_ms > (QUESTION_TIMEOUT_SEC * 1000 + LATENCY_BUFFER_MS):
                last_answer.is_late = True
                last_answer.is_correct = False
                last_answer.answered_at = now
                last_answer.response_ms = int(elapsed_ms)
                db.commit()

    position_count = len(served_answers)

    if position_count >= 20:
        return {"finished": True, "total": 20}

    tp_all_qs = _get_tp_questions_dict(db, attempt.tp_id)
    q_map = {q["id"]: q for q in tp_all_qs}

    if served_answers and served_answers[-1].answered_at is None:
        current = served_answers[-1]
        q = q_map.get(current.question_id)
        if not q:
            raw_q = db.query(Question).filter(Question.id == current.question_id).first()
            q = {"id": raw_q.id, "text": raw_q.text} if raw_q else {"id": current.question_id, "text": "Question"}
        options_order = [True, False]
        random.shuffle(options_order)
        return {
            "finished": False,
            "question_id": q["id"],
            "text": q["text"],
            "options": options_order,
            "position": current.position,
            "total": 20
        }

    served_q_ids = {ans.question_id for ans in served_answers}
    served_questions = [q_map[qid] for qid in served_q_ids if qid in q_map]

    served_trap_groups = {}
    for sq in served_questions:
        if sq["trap_group_id"] is not None:
            ans_pos = next(a.position for a in served_answers if a.question_id == sq["id"])
            served_trap_groups[sq["trap_group_id"]] = (sq["trap_mode"], ans_pos)

    candidates = [q for q in tp_all_qs if q["id"] not in served_q_ids]
    valid_candidates = []
    next_position = position_count + 1

    for cand in candidates:
        if cand["trap_group_id"] is not None and cand["trap_group_id"] in served_trap_groups:
            mode, served_pos = served_trap_groups[cand["trap_group_id"]]
            if mode == "hidden":
                continue
            elif mode == "attention_check":
                if next_position < served_pos + 4:
                    continue

        valid_candidates.append(cand)

    if not valid_candidates:
        valid_candidates = candidates

    if not valid_candidates:
        raise HTTPException(status_code=400, detail="No eligible questions available in bank.")

    next_q = random.choice(valid_candidates)

    new_ans = AttemptAnswer(
        attempt_id=attempt.id,
        question_id=next_q["id"],
        position=next_position,
        shown_at=now,
        chosen=None,
        is_correct=None,
        is_late=False
    )
    db.add(new_ans)
    db.commit()
    db.refresh(new_ans)

    options_order = [True, False]
    random.shuffle(options_order)

    return {
        "finished": False,
        "question_id": next_q["id"],
        "text": next_q["text"],
        "options": options_order,
        "position": next_position,
        "total": 20
    }

@router.post("/attempt/{attempt_id}/answer-and-next")
def answer_and_next(
    attempt_id: int,
    req_data: AnswerSubmitRequest,
    db: DBSession = Depends(get_db)
):
    attempt = db.query(Attempt).filter(Attempt.id == attempt_id).first()
    if not attempt or attempt.status != "in_progress":
        raise HTTPException(status_code=400, detail="Attempt invalid or not in progress.")

    now = datetime.utcnow()
    tp_all_qs = _get_tp_questions_dict(db, attempt.tp_id)
    q_map = {q["id"]: q for q in tp_all_qs}

    # 1. Process current answer
    ans_row = db.query(AttemptAnswer).filter(
        AttemptAnswer.attempt_id == attempt_id,
        AttemptAnswer.question_id == req_data.question_id
    ).first()

    if ans_row and ans_row.answered_at is None:
        elapsed_ms = int((now - ans_row.shown_at).total_seconds() * 1000)
        ans_row.response_ms = elapsed_ms
        ans_row.answered_at = now
        ans_row.chosen = req_data.chosen

        max_allowed_ms = (QUESTION_TIMEOUT_SEC * 1000) + LATENCY_BUFFER_MS
        if elapsed_ms > max_allowed_ms:
            ans_row.is_late = True
            ans_row.is_correct = False
        else:
            ans_row.is_late = False
            if req_data.chosen is None:
                ans_row.is_correct = None
            else:
                question = q_map.get(req_data.question_id)
                if question is not None:
                    ans_row.is_correct = (req_data.chosen == question["correct_answer"])
                else:
                    ans_row.is_correct = False

    # 2. Immediately sample next question in the SAME transaction
    served_answers = db.query(AttemptAnswer).filter(
        AttemptAnswer.attempt_id == attempt_id
    ).order_by(AttemptAnswer.position).all()

    position_count = len(served_answers)
    if position_count >= 20:
        db.commit()
        return {
            "received": True,
            "next_question": {"finished": True, "total": 20}
        }

    served_q_ids = {ans.question_id for ans in served_answers}
    served_questions = [q_map[qid] for qid in served_q_ids if qid in q_map]

    served_trap_groups = {}
    for sq in served_questions:
        if sq["trap_group_id"] is not None:
            ans_pos = next(a.position for a in served_answers if a.question_id == sq["id"])
            served_trap_groups[sq["trap_group_id"]] = (sq["trap_mode"], ans_pos)

    candidates = [q for q in tp_all_qs if q["id"] not in served_q_ids]
    valid_candidates = []
    next_position = position_count + 1

    for cand in candidates:
        if cand["trap_group_id"] is not None and cand["trap_group_id"] in served_trap_groups:
            mode, served_pos = served_trap_groups[cand["trap_group_id"]]
            if mode == "hidden":
                continue
            elif mode == "attention_check":
                if next_position < served_pos + 4:
                    continue
        valid_candidates.append(cand)

    if not valid_candidates:
        valid_candidates = candidates

    if not valid_candidates:
        db.commit()
        raise HTTPException(status_code=400, detail="No eligible questions available in bank.")

    next_q = random.choice(valid_candidates)

    new_ans = AttemptAnswer(
        attempt_id=attempt.id,
        question_id=next_q["id"],
        position=next_position,
        shown_at=now,
        chosen=None,
        is_correct=None,
        is_late=False
    )
    db.add(new_ans)
    db.commit()

    options_order = [True, False]
    random.shuffle(options_order)

    return {
        "received": True,
        "next_question": {
            "finished": False,
            "question_id": next_q["id"],
            "text": next_q["text"],
            "options": options_order,
            "position": next_position,
            "total": 20
        }
    }

@router.post("/attempt/{attempt_id}/answer", response_model=AnswerSubmitResponse)
def submit_answer(
    attempt_id: int,
    req_data: AnswerSubmitRequest,
    db: DBSession = Depends(get_db)
):
    attempt = db.query(Attempt).filter(Attempt.id == attempt_id).first()
    if not attempt or attempt.status != "in_progress":
        raise HTTPException(status_code=400, detail="Attempt invalid or not in progress.")

    ans_row = db.query(AttemptAnswer).filter(
        AttemptAnswer.attempt_id == attempt_id,
        AttemptAnswer.question_id == req_data.question_id
    ).first()

    if not ans_row:
        raise HTTPException(status_code=404, detail="Question answer slot not found.")

    if ans_row.answered_at is not None:
        return {"received": True}

    now = datetime.utcnow()
    elapsed_ms = int((now - ans_row.shown_at).total_seconds() * 1000)
    ans_row.response_ms = elapsed_ms
    ans_row.answered_at = now
    ans_row.chosen = req_data.chosen

    max_allowed_ms = (QUESTION_TIMEOUT_SEC * 1000) + LATENCY_BUFFER_MS
    if elapsed_ms > max_allowed_ms:
        ans_row.is_late = True
        ans_row.is_correct = False
    else:
        ans_row.is_late = False
        if req_data.chosen is None:
            ans_row.is_correct = None
        else:
            tp_all_qs = _get_tp_questions_dict(db, attempt.tp_id)
            q_map = {q["id"]: q for q in tp_all_qs}
            question = q_map.get(req_data.question_id)
            if question is not None:
                ans_row.is_correct = (req_data.chosen == question["correct_answer"])
            else:
                ans_row.is_correct = False

    db.commit()
    return {"received": True}

@router.post("/attempt/{attempt_id}/event", response_model=ViolationEventResponse)
def log_violation_event(
    attempt_id: int,
    req_data: ViolationEventRequest,
    db: DBSession = Depends(get_db)
):
    attempt = db.query(Attempt).filter(Attempt.id == attempt_id).first()
    if not attempt:
        raise HTTPException(status_code=404, detail="Attempt not found.")

    if attempt.status != "in_progress":
        return {
            "violation_count": getattr(attempt, "violation_count", 0) or 0,
            "auto_failed": True,
            "message": "Attempt already finished."
        }

    now = datetime.utcnow()
    current_count = (getattr(attempt, "violation_count", 0) or 0) + 1
    attempt.violation_count = current_count

    log_list = []
    if attempt.violation_log:
        try:
            log_list = json.loads(attempt.violation_log)
        except Exception:
            log_list = []

    timestamp_str = now.strftime("%H:%M:%S")
    log_entry = f"{timestamp_str} - {req_data.event_type}"
    if req_data.details:
        log_entry += f" ({req_data.details})"
    log_list.append(log_entry)
    attempt.violation_log = json.dumps(log_list)

    auto_failed = False
    msg = f"Violation recorded ({current_count}/4)."

    if current_count >= 4:
        auto_failed = True
        attempt.status = "finished"
        attempt.score = 0.0
        attempt.flagged = True
        attempt.ended_at = now
        msg = "4 violations recorded. Test automatically failed (Score 0.0/20)."

        answers = db.query(AttemptAnswer).filter(AttemptAnswer.attempt_id == attempt_id).all()
        for ans in answers:
            if ans.answered_at is None:
                ans.answered_at = now
                ans.chosen = None
                ans.is_late = False
                ans.is_correct = None

    db.commit()
    return {
        "violation_count": current_count,
        "auto_failed": auto_failed,
        "message": msg
    }

@router.post("/attempt/{attempt_id}/finish", response_model=FinishAttemptResponse)
def finish_attempt(attempt_id: int, db: DBSession = Depends(get_db)):
    attempt = db.query(Attempt).filter(Attempt.id == attempt_id).first()
    if not attempt:
        raise HTTPException(status_code=404, detail="Attempt not found.")

    now = datetime.utcnow()
    answers = db.query(AttemptAnswer).filter(AttemptAnswer.attempt_id == attempt_id).all()

    # Finalize any unsubmitted questions as unanswered (chosen = None -> 0 pts)
    for ans in answers:
        if ans.answered_at is None:
            ans.answered_at = now
            ans.chosen = None
            ans.is_late = False
            ans.is_correct = None

    correct_count = sum(1 for a in answers if a.is_correct is True and not a.is_late)
    wrong_or_late_count = sum(1 for a in answers if (a.is_correct is False or a.is_late) and a.chosen is not None)
    skipped_count = sum(1 for a in answers if a.chosen is None)

    # Raw score: +1 for correct, -1 for wrong/late, 0 for skipped/unanswered
    raw_score = float(correct_count - wrong_or_late_count)
    final_mark = max(0.0, min(20.0, raw_score))

    # If 4 or more violations recorded OR exited early before answering 20 questions, set score = 0.0 & flag
    if (getattr(attempt, "violation_count", 0) or 0) >= 4 or len(answers) < 20:
        final_mark = 0.0
        raw_score = 0.0
        attempt.flagged = True

    attempt.score = final_mark
    attempt.ended_at = now
    attempt.status = "finished"

    db.commit()

    return {
        "final_mark": round(final_mark, 2),
        "raw_score": raw_score,
        "correct_count": correct_count,
        "wrong_count": wrong_or_late_count,
        "skipped_count": skipped_count,
        "status": "finished"
    }

@router.post("/dev/reset_cooldown")
def reset_cooldown(code: Optional[str] = None, db: DBSession = Depends(get_db)):
    """Developer route to reset active cooldowns without deleting attempt history."""
    past_time = datetime.utcnow() - timedelta(minutes=15)
    if code:
        clean_code = code.strip().upper()
        attempts = db.query(Attempt).filter(Attempt.code == clean_code, Attempt.status == "finished").all()
    else:
        attempts = db.query(Attempt).filter(Attempt.status == "finished").all()

    for att in attempts:
        att.ended_at = past_time
    db.commit()

    return {"message": "Cooldown reset successfully without deleting attempt history."}
