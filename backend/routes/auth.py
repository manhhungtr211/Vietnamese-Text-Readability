# backend/routes/auth.py
from fastapi import APIRouter, HTTPException
from backend.models.auth import RegisterInput
import sqlite3
from hashlib import sha256
import os

router = APIRouter()

DB_PATH = os.path.join(os.path.dirname(__file__), '../database/chat_history.db')

def hash_password(password: str) -> str:
    return sha256(password.encode()).hexdigest()

@router.post("/register")
def register(data: RegisterInput):
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Check email đã tồn tại chưa
        cursor.execute("SELECT * FROM USER WHERE email = ?", (data.username,))
        existing = cursor.fetchone()
        if existing:
            raise HTTPException(status_code=400, detail="Email đã tồn tại.")

        # Thêm user mới
        hashed = hash_password(data.password)
        cursor.execute(
            "INSERT INTO USER (email, full_name, password) VALUES (?, ?, ?)",
            (data.username, data.full_name, hashed)
        )

        conn.commit()
        conn.close()

        return {"success": True, "message": "Đăng ký thành công!"}
    
    except Exception as e:
        return {"success": False, "message": f"Lỗi: {str(e)}"}
