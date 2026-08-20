#!/usr/bin/env python3
import os
import sys
import json
import re

# Ensure scripts directory is in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from qbank.tp1 import get_tp1_questions
from qbank.tp2 import get_tp2_questions
from qbank.tp3 import get_tp3_questions
from qbank.tp4 import get_tp4_questions
from qbank.tp5 import get_tp5_questions
from qbank.tp6 import get_tp6_questions

PROHIBITED_KEYWORDS = [
    "DBSCAN",
    "Density-Based",
    "density-based",
    "K-Means++",
    "k-means++",
    "minPts",
    "min_pts",
    "epsilon",
    "core point",
    "border point",
    "noise point"
]

TP_FILE_MAP = {
    1: ("tp1_data_cleaning.json", "Raw Data Cleaning", get_tp1_questions),
    2: ("tp2_eda_visualization.json", "Exploratory Data Analysis and Visualization", get_tp2_questions),
    3: ("tp3_feature_engineering.json", "Data Preprocessing, Feature Engineering and Selection", get_tp3_questions),
    4: ("tp4_classification.json", "Model Evaluation & Performance Metrics", get_tp4_questions),
    5: ("tp5_regression.json", "Supervised Classification Algorithms & Training", get_tp5_questions),
    6: ("tp6_clustering.json", "Unsupervised Learning, Clustering & Association Rules", get_tp6_questions)
}

def audit_and_build():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(project_root, "data", "question_bank")
    os.makedirs(output_dir, exist_ok=True)

    all_questions_master = []
    seen_ids = set()
    index_manifest = {"tps": {}, "total_questions": 0}

    print("=== STARTING QUESTION BANK RECONSTRUCTION AND AUDIT ===")

    for tp_id in range(1, 7):
        filename, title, getter_func = TP_FILE_MAP[tp_id]
        qs = getter_func()

        # 1. Count validation
        total_count = len(qs)
        normal_count = sum(1 for q in qs if q["category"] == "normal")
        tricky_count = sum(1 for q in qs if q["category"] == "tricky")
        trap_count = sum(1 for q in qs if q["category"] == "trap")

        print(f"\n[TP {tp_id}] {title}")
        print(f"  Count: {total_count} / 200 (Normal: {normal_count}, Tricky: {tricky_count}, Trap: {trap_count})")

        assert total_count == 200, f"TP{tp_id} must have exactly 200 questions, found {total_count}"
        assert normal_count == 90, f"TP{tp_id} must have exactly 90 normal questions, found {normal_count}"
        assert tricky_count == 50, f"TP{tp_id} must have exactly 50 tricky questions, found {tricky_count}"
        assert trap_count == 60, f"TP{tp_id} must have exactly 60 trap questions, found {trap_count}"

        # 2. Individual Question Format & Prohibited Keyword Audit
        formatted_tp_qs = []
        for idx, q in enumerate(qs, 1):
            q_id = q.get("id")
            assert q_id not in seen_ids, f"Duplicate Question ID detected: {q_id}"
            seen_ids.add(q_id)

            assert isinstance(q.get("answer"), bool), f"Question {q_id} answer must be boolean True/False"
            assert q.get("category") in ["normal", "tricky", "trap"], f"Question {q_id} invalid category"
            assert len(q.get("question", "").strip()) > 10, f"Question {q_id} text too short"
            assert len(q.get("explanation", "").strip()) > 10, f"Question {q_id} explanation too short"

            # Check Prohibited Keywords
            full_text = (q["question"] + " " + q["explanation"]).lower()
            for kw in PROHIBITED_KEYWORDS:
                if kw.lower() in full_text:
                    raise ValueError(f"CRITICAL AUDIT FAILURE: Prohibited keyword '{kw}' found in Question {q_id}!")

            item = {
                "id": q_id,
                "tp": tp_id,
                "category": q["category"],
                "question": q["question"].strip(),
                "answer": q["answer"],
                "explanation": q["explanation"].strip()
            }
            formatted_tp_qs.append(item)
            all_questions_master.append(item)

        # Write TP JSON file
        tp_file_path = os.path.join(output_dir, filename)
        with open(tp_file_path, "w", encoding="utf-8") as f:
            json.dump(formatted_tp_qs, f, indent=2, ensure_ascii=False)

        # Add to index manifest
        index_manifest["tps"][str(tp_id)] = {
            "title": title,
            "filename": filename,
            "total": total_count,
            "categories": {
                "normal": normal_count,
                "tricky": tricky_count,
                "trap": trap_count
            }
        }

    index_manifest["total_questions"] = len(all_questions_master)

    # Write index.json
    index_path = os.path.join(output_dir, "index.json")
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index_manifest, f, indent=2, ensure_ascii=False)

    # Write master consolidated data/question_bank.json for database sync
    master_json_path = os.path.join(project_root, "data", "question_bank.json")
    with open(master_json_path, "w", encoding="utf-8") as f:
        json.dump(all_questions_master, f, indent=2, ensure_ascii=False)

    print("\n=======================================================")
    print("SUCCESS! Question Bank Reconstructed & Audited Perfectly:")
    print(f"Total Questions: {len(all_questions_master)} / 1,200")
    print(f"TP Files Written to: {output_dir}")
    print("Zero Prohibited Keywords Detected (DBSCAN & K-Means++ = 0)")
    print("=======================================================")

if __name__ == "__main__":
    audit_and_build()
