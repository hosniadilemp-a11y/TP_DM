#!/usr/bin/env bash
set -e

STUDENT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$STUDENT_DIR")"
cd "$PROJECT_ROOT"

echo "======================================================================"
echo "🚀 Data Mining TP Continuous Student Evaluation Engine Startup"
echo "======================================================================"

export PYTHONPATH="$PROJECT_ROOT:$STUDENT_DIR"

if [ ! -f "data/tp_eval.db" ]; then
    echo "🌱 Seeding database for first run..."
    python scripts/seed_db.py
fi

PORT=8503
echo "🔍 Checking for process running on port $PORT..."
PID=$(lsof -ti:$PORT || true)
if [ -n "$PID" ]; then
    echo "⚠️ Terminating old process on port $PORT (PID: $PID)..."
    kill -9 $PID || true
    echo "✅ Port $PORT freed."
fi

echo "🌐 Launching Student FastAPI server on http://localhost:$PORT..."
exec python -m uvicorn student_app.app.main:app --host 0.0.0.0 --port $PORT --reload
