# backend/routes/analyze.py
from fastapi import APIRouter
from models.login import TextInput, HistoryInput
import os
import json

router = APIRouter()
HISTORY_PATH = os.path.join(os.path.dirname(__file__), '../db/history.json')

def load_history():
    if not os.path.exists(HISTORY_PATH):
        return {}
    with open(HISTORY_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_history(history):
    with open(HISTORY_PATH, 'w', encoding='utf-8') as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

@router.post("/analyze")
def analyze(data: TextInput):
    # Dummy NLP logic
    difficulty = "Dễ" if len(data.text) < 50 else "Khó"
    highlighted_text = data.text.replace("khó", "<b>khó</b>")
    # Save to history (for demo, username is not handled)
    history = load_history()
    user = "demo_user"  # Replace with actual user if needed
    if user not in history:
        history[user] = []
    history[user].append(data.text)
    save_history(history)
    return {"difficulty": difficulty, "highlighted_text": highlighted_text}

@router.get("/analyze/history")
def get_history(username: str):
    history = load_history()
    return {"history": history.get(username, [])}
