import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from student_app.app.main import app
from student_app.app.database import Base, get_db
from student_app.app.models import ValidCode, TP, Question, Session, Attempt, AttemptAnswer

# In-memory SQLite DB for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    
    # Seed Student Codes
    db.add(ValidCode(code="IASD01", group_code="IASD", active=True))
    db.add(ValidCode(code="SIAD01", group_code="SIAD", active=True))
    db.add(ValidCode(code="INACTIVE01", group_code="IASD", active=False))
    
    # Seed TP
    tp1 = TP(id=1, name="TP 1: Data Cleaning", ordering=1)
    db.add(tp1)
    
    # Seed Active Session
    from datetime import datetime, timedelta
    now = datetime.utcnow()
    sess = Session(tp_id=1, opens_at=now - timedelta(days=1), closes_at=now + timedelta(days=1))
    db.add(sess)
    
    # Seed 25 Questions for TP1
    for i in range(1, 26):
        db.add(Question(
            tp_id=1,
            topic_id=1,
            text=f"Question {i} test text",
            correct_answer=(i % 2 == 0),
            trap_group_id=None,
            trap_mode=None,
            active=True
        ))
    
    db.commit()
    db.close()
    yield
    Base.metadata.drop_all(bind=engine)

def test_invalid_student_code_rejected():
    res = client.post("/api/attempt/start", json={"code": "INVALID99", "tp_id": 1})
    assert res.status_code == 400
    assert "Wrong student code" in res.json()["detail"]

def test_inactive_student_code_rejected():
    res = client.post("/api/attempt/start", json={"code": "INACTIVE01", "tp_id": 1})
    assert res.status_code == 400

def test_valid_start_attempt():
    res = client.post("/api/attempt/start", json={"code": "IASD01", "tp_id": 1})
    assert res.status_code == 200
    data = res.json()
    assert "attempt_id" in data
    assert isinstance(data["attempt_id"], int)

def test_cooldown_enforcement():
    # 1. First attempt starts
    res1 = client.post("/api/attempt/start", json={"code": "SIAD01", "tp_id": 1})
    assert res1.status_code == 200
    att_id1 = res1.json()["attempt_id"]

    # Re-starting while in_progress RESUMES the attempt with same ID
    res_resume = client.post("/api/attempt/start", json={"code": "SIAD01", "tp_id": 1})
    assert res_resume.status_code == 200
    assert res_resume.json()["attempt_id"] == att_id1

    # Finish the attempt
    client.post(f"/api/attempt/{att_id1}/finish")

    # Starting a new attempt within 10 mins of finished attempt fails with 429
    res2 = client.post("/api/attempt/start", json={"code": "SIAD01", "tp_id": 1})
    assert res2.status_code == 429
    assert "Cooldown active" in res2.json()["detail"]

def test_zero_answer_leakage_in_question_payload():
    # Start attempt
    start_res = client.post("/api/attempt/start", json={"code": "IASD01", "tp_id": 1})
    attempt_id = start_res.json()["attempt_id"]

    # Fetch next question
    q_res = client.get(f"/api/attempt/{attempt_id}/next-question")
    assert q_res.status_code == 200
    q_data = q_res.json()

    # Verify no correct_answer, trap_group_id, or trap_mode leak in HTTP response
    assert "question_id" in q_data
    assert "text" in q_data
    assert "correct_answer" not in q_data
    assert "trap_group_id" not in q_data
    assert "trap_mode" not in q_data

def test_full_quiz_lifecycle_and_score():
    start_res = client.post("/api/attempt/start", json={"code": "IASD01", "tp_id": 1})
    attempt_id = start_res.json()["attempt_id"]

    for _ in range(20):
        q_res = client.get(f"/api/attempt/{attempt_id}/next-question")
        q_data = q_res.json()
        assert q_data["finished"] is False

        # Submit answer (True)
        ans_res = client.post(f"/api/attempt/{attempt_id}/answer", json={
            "question_id": q_data["question_id"],
            "chosen": True
        })
        assert ans_res.status_code == 200
        assert ans_res.json()["received"] is True

    # 21st call returns finished
    fin_q = client.get(f"/api/attempt/{attempt_id}/next-question")
    assert fin_q.json()["finished"] is True

    # Finish attempt
    finish_res = client.post(f"/api/attempt/{attempt_id}/finish")
    assert finish_res.status_code == 200
    f_data = finish_res.json()
    assert "final_mark" in f_data
    assert 0.0 <= f_data["final_mark"] <= 20.0

def test_skipped_question_scores_zero():
    start_res = client.post("/api/attempt/start", json={"code": "SIAD01", "tp_id": 1})
    attempt_id = start_res.json()["attempt_id"]

    for _ in range(20):
        q_res = client.get(f"/api/attempt/{attempt_id}/next-question")
        q_data = q_res.json()
        if q_data["finished"]:
            break

        # Submit explicit skip (chosen = None)
        client.post(f"/api/attempt/{attempt_id}/answer", json={
            "question_id": q_data["question_id"],
            "chosen": None
        })

    finish_res = client.post(f"/api/attempt/{attempt_id}/finish")
    assert finish_res.status_code == 200
    f_data = finish_res.json()
    assert f_data["raw_score"] == 0.0
    assert f_data["final_mark"] == 0.0
    assert f_data["skipped_count"] == 20
