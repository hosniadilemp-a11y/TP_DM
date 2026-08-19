from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from student_app.app.database import Base

class ValidCode(Base):
    __tablename__ = "valid_codes"

    code = Column(String, primary_key=True, index=True)
    group_code = Column(String, nullable=False)
    active = Column(Boolean, default=True, nullable=False)

class TP(Base):
    __tablename__ = "tp"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    ordering = Column(Integer, nullable=False)

    topics = relationship("Topic", back_populates="tp")
    questions = relationship("Question", back_populates="tp")

class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    tp_id = Column(Integer, ForeignKey("tp.id"), nullable=False)
    name = Column(String, nullable=False)

    tp = relationship("TP", back_populates="topics")
    questions = relationship("Question", back_populates="topic")

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    tp_id = Column(Integer, ForeignKey("tp.id"), nullable=False)
    topic_id = Column(Integer, ForeignKey("topics.id"), nullable=False)
    text = Column(String, nullable=False)
    correct_answer = Column(Boolean, nullable=False)
    trap_group_id = Column(Integer, nullable=True)
    trap_mode = Column(String, nullable=True) # 'hidden' or 'attention_check'
    active = Column(Boolean, default=True, nullable=False)
    retired_at = Column(DateTime, nullable=True)

    tp = relationship("TP", back_populates="questions")
    topic = relationship("Topic", back_populates="questions")

class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    tp_id = Column(Integer, ForeignKey("tp.id"), nullable=False)
    opens_at = Column(DateTime, nullable=False)
    closes_at = Column(DateTime, nullable=False)

class Attempt(Base):
    __tablename__ = "attempts"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, ForeignKey("valid_codes.code"), nullable=False)
    tp_id = Column(Integer, ForeignKey("tp.id"), nullable=False)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=True)
    started_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    ended_at = Column(DateTime, nullable=True)
    status = Column(String, default="in_progress", nullable=False) # 'in_progress', 'finished', 'abandoned'
    score = Column(Float, nullable=True) # Raw score (-20 to +20)
    device_fingerprint = Column(String, nullable=True)
    client_ip = Column(String, nullable=True)
    ip_hash = Column(String, nullable=True)
    user_agent = Column(String, nullable=True)
    flagged = Column(Boolean, default=False, nullable=False)
    excluded_from_score = Column(Boolean, default=False, nullable=False)

    answers = relationship("AttemptAnswer", back_populates="attempt")

class AttemptAnswer(Base):
    __tablename__ = "attempt_answers"

    id = Column(Integer, primary_key=True, index=True)
    attempt_id = Column(Integer, ForeignKey("attempts.id"), nullable=False)
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    position = Column(Integer, nullable=False) # 1..20
    shown_at = Column(DateTime, nullable=False)
    answered_at = Column(DateTime, nullable=True)
    chosen = Column(Boolean, nullable=True)
    is_correct = Column(Boolean, nullable=True)
    response_ms = Column(Integer, nullable=True)
    is_late = Column(Boolean, default=False, nullable=False)

    attempt = relationship("Attempt", back_populates="answers")
    question = relationship("Question")
