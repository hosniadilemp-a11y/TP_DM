import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

APP_DIR = os.path.dirname(os.path.abspath(__file__))
STUDENT_APP_DIR = os.path.dirname(APP_DIR)
PROJECT_ROOT = os.path.dirname(STUDENT_APP_DIR)
DEFAULT_DB_PATH = os.path.join(PROJECT_ROOT, "data", "tp_eval.db")
os.makedirs(os.path.dirname(DEFAULT_DB_PATH), exist_ok=True)

DATABASE_URL = os.getenv("DATABASE_URL", f"sqlite:///{DEFAULT_DB_PATH}")

# Fix postgresql:// prefix if using old psycopg2 style on Render
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
