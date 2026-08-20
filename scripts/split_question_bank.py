#!/usr/bin/env python3
"""
Splits data/question_bank.json into topic-specific JSON files in data/question_bank/
and generates an index metadata file with analytics summaries.
"""

import os
import json
from collections import defaultdict

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER_BANK_PATH = os.path.join(PROJECT_ROOT, "data", "question_bank.json")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "data", "question_bank")

TP_META = {
    1: {"name": "Data Cleaning & Preparation", "filename": "tp1_data_cleaning.json"},
    2: {"name": "Exploratory Data Analysis & Visualization", "filename": "tp2_eda_visualization.json"},
    3: {"name": "Feature Engineering & Selection", "filename": "tp3_feature_engineering.json"},
    4: {"name": "Supervised Learning — Classification", "filename": "tp4_classification.json"},
    5: {"name": "Supervised Learning — Regression", "filename": "tp5_regression.json"},
    6: {"name": "Unsupervised Learning & Clustering", "filename": "tp6_clustering.json"}
}

def split_questions():
    if not os.path.exists(MASTER_BANK_PATH):
        print(f"Error: Master question bank not found at {MASTER_BANK_PATH}")
        return

    with open(MASTER_BANK_PATH, "r", encoding="utf-8") as f:
        questions = json.load(f)

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    by_tp = defaultdict(list)
    for idx, q in enumerate(questions, 1):
        q_copy = dict(q)
        q_copy["id"] = idx
        tp_id = q_copy.get("tp_id", 1)
        by_tp[tp_id].append(q_copy)

    index_summary = {
        "total_questions": len(questions),
        "tp_summary": []
    }

    for tp_id, meta in TP_META.items():
        tp_qs = by_tp.get(tp_id, [])
        file_path = os.path.join(OUTPUT_DIR, meta["filename"])
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(tp_qs, f, indent=2, ensure_ascii=False)

        plain_count = sum(1 for q in tp_qs if q.get("question_type") == "plain")
        trick_count = sum(1 for q in tp_qs if q.get("question_type") == "trick")
        trap_count = sum(1 for q in tp_qs if q.get("question_type") == "trap")
        true_count = sum(1 for q in tp_qs if q.get("correct_answer") is True)
        false_count = sum(1 for q in tp_qs if q.get("correct_answer") is False)

        index_summary["tp_summary"].append({
            "tp_id": tp_id,
            "name": meta["name"],
            "filename": meta["filename"],
            "total_questions": len(tp_qs),
            "plain_count": plain_count,
            "trick_count": trick_count,
            "trap_count": trap_count,
            "true_count": true_count,
            "false_count": false_count
        })

        print(f"✅ Saved {len(tp_qs)} questions to data/question_bank/{meta['filename']}")

    # Save index.json
    index_path = os.path.join(OUTPUT_DIR, "index.json")
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index_summary, f, indent=2, ensure_ascii=False)

    print(f"📊 Saved index metadata to data/question_bank/index.json")

if __name__ == "__main__":
    split_questions()
