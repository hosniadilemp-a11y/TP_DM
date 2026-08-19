#!/usr/bin/env python3
"""
Database Seeder for TP Continuous Evaluation App.
Populates:
- 400 Student Codes (SIAD01..100, IASD01..100, RSD01..100, CS01..100)
- 6 TPs and 18 Topics
- Open Sessions for all TPs
- 1000 True/False Questions from data/question_bank.json
"""

import json
import os
from datetime import datetime, timedelta
from student_app.app.database import engine, Base, SessionLocal
from student_app.app.models import ValidCode, TP, Topic, Question, Session

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUESTION_BANK_PATH = os.path.join(PROJECT_ROOT, "data", "question_bank.json")

def seed_database():
    print("🌱 Initializing database schema...")
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        # 1. Seed Valid Codes (SIAD, IASD, RSD, CS 01..100)
        print("👥 Seeding valid student codes...")
        groups = ["SIAD", "IASD", "RSD", "CS"]
        existing_codes = {c.code for c in db.query(ValidCode).all()}
        new_codes = []
        for g in groups:
            for i in range(1, 101):
                code_str = f"{g}{i:02d}"
                if code_str not in existing_codes:
                    new_codes.append(ValidCode(code=code_str, group_code=g, active=True))
        if new_codes:
            db.add_all(new_codes)
            db.commit()
        print(f"  ✓ {len(new_codes)} new student codes seeded (total: {db.query(ValidCode).count()})")

        # 2. Seed TPs and Topics
        print("📚 Seeding TPs and Topics...")
        tp_data = [
            (1, "TP 1: Data Cleaning & Preparation", ["Missing Values Handling", "Outlier Detection (IQR & Z-score)", "Deduplication & Integrity"]),
            (2, "TP 2: Exploratory Data Analysis (EDA)", ["Summary Statistics & Skewness", "Correlation Analysis", "Visualizations (Boxplots/Histograms)"]),
            (3, "TP 3: Data Preprocessing & Feature Engineering", ["Feature Scaling", "Categorical Encoding", "Dimensionality Reduction (PCA)"]),
            (4, "TP 4: Model Evaluation Metrics", ["Confusion Matrix & Metrics", "Precision, Recall & F1-Score", "ROC-AUC & Cross-Validation"]),
            (5, "TP 5: Supervised Classification Models", ["Decision Trees & Entropy", "Ensemble Methods (Random Forest)", "KNN, SVM & Naive Bayes"]),
            (6, "TP 6: Clustering & Association Rules", ["K-Means & Silhouette Analysis", "Hierarchical Clustering & Dendrograms", "Association Rules (Apriori)"])
        ]

        for tp_id, tp_name, topics_list in tp_data:
            existing_tp = db.query(TP).filter(TP.id == tp_id).first()
            if not existing_tp:
                tp_obj = TP(id=tp_id, name=tp_name, ordering=tp_id)
                db.add(tp_obj)
                db.commit()

            for idx, top_name in enumerate(topics_list, 1):
                top_id = (tp_id - 1) * 3 + idx
                existing_top = db.query(Topic).filter(Topic.id == top_id).first()
                if not existing_top:
                    db.add(Topic(id=top_id, tp_id=tp_id, name=top_name))
            db.commit()

        # 3. Seed Open Sessions (Always active for testing)
        print("⏰ Seeding active sessions...")
        now = datetime.utcnow()
        opens_at = now - timedelta(days=30)
        closes_at = now + timedelta(days=365)

        for tp_id in range(1, 7):
            existing_sess = db.query(Session).filter(Session.tp_id == tp_id).first()
            if not existing_sess:
                db.add(Session(tp_id=tp_id, opens_at=opens_at, closes_at=closes_at))
        db.commit()

        # 4. Seed Questions & Ensure Topics Exist
        print("❓ Seeding 1000 question bank...")
        if not os.path.exists(QUESTION_BANK_PATH):
            raise FileNotFoundError(f"Question bank file not found at {QUESTION_BANK_PATH}. Run scripts/generate_questions.py first!")

        with open(QUESTION_BANK_PATH, "r", encoding="utf-8") as f:
            questions_list = json.load(f)

        existing_topic_ids = {t.id for t in db.query(Topic).all()}
        for q in questions_list:
            tid = q["topic_id"]
            tpid = q["tp_id"]
            if tid not in existing_topic_ids:
                existing_topic_ids.add(tid)
                db.add(Topic(id=tid, tp_id=tpid, name=f"Topic {tid}"))
        db.commit()

        db.query(Question).delete()
        db.commit()

        q_objects = []
        for q in questions_list:
            q_objects.append(Question(
                tp_id=q["tp_id"],
                topic_id=q["topic_id"],
                text=q["text"],
                correct_answer=q["correct_answer"],
                trap_group_id=q.get("trap_group_id"),
                trap_mode=q.get("trap_mode"),
                active=True
            ))
        db.add_all(q_objects)
        db.commit()

        print(f"  ✓ {db.query(Question).count()} questions active in database")
        print("✅ Database seeding complete!")

    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
