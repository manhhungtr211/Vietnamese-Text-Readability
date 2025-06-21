# backend/routes/auth.py
from fastapi import APIRouter, HTTPException
from backend.models.auth import LoginInput
from backend.utils import session 
import sqlite3, os
from hashlib import sha256

router = APIRouter()
DB_PATH = os.path.join(os.path.dirname(__file__), '../database/chat_history.db')

def hash_password(password: str) -> str:
    return sha256(password.encode()).hexdigest()

@router.post("/login")
def handle_login(data: LoginInput):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT user_id, email, full_name, password FROM USER WHERE email = ?", (data.username,))
    user = cursor.fetchone()
    conn.close()

    if user and user[3] == hash_password(data.password):
        session_id = session.create_session({"user_id": user[0], "email": user[1], "full_name": user[2]})
        return {
            "success": True, 
            "full_name": user[2],
            "session_id": session_id}
    
    raise HTTPException(status_code=401, detail="Sai email hoặc mật khẩu")
