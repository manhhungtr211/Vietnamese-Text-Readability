# backend/routes/auth.py
from fastapi import APIRouter, HTTPException
from backend.models.auth import LogoutInput
from backend.utils import session 
import sqlite3, os

router = APIRouter()

@router.post("/logout")
def handle_logout(data: LogoutInput):
    try:
        session.delete_session(data.session_id)
        return {"success": True, "message": "Đăng xuất thành công!"}
        
    except Exception as e: 
        raise HTTPException(status_code=500, detail=f"Lỗi: {str(e)}")