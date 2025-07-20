#!/bin/bash
set -e

if [ -f venv/bin/activate ]; then
  source venv/bin/activate
else
  python3 -m venv venv
  source venv/bin/activate
fi

pip install --upgrade pip > /dev/null
pip install fastapi uvicorn requests > /dev/null

echo "Starting FastAPI app in background..."
nohup uvicorn app.main:app --host 0.0.0.0 --port 8000 > uvicorn.log 2>&1 &

sleep 3

echo "Environment is set up."
