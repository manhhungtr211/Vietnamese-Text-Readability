# FE/api.py
import requests
from config import API_URL

def analyze_text(text: str, session_id=None, conversation_id=None):
    try:
        payload = {"text": text}
        if session_id:
            payload["session_id"] = session_id
        if conversation_id:
            payload["conversation_id"] = conversation_id
        resp = requests.post(f"{API_URL}/analyze", json=payload)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"error": resp.json().get("detail", "Lỗi không xác định")}
    except Exception as e:
        return {"error": str(e)}

def login_user(username, password):
    try:
        resp = requests.post(f"{API_URL}/login", json={"username": username, "password": password})
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"success": False, "message": resp.json().get("detail", "Sai tài khoản hoặc mật khẩu.")}
    except Exception as e:
        return {"success": False, "message": str(e)}

def register_user(username, full_name, password):
    try:
        resp = requests.post(f"{API_URL}/register", json={"username": username, "full_name": full_name, "password": password})
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"success": False, "message": resp.json().get("detail", "Lỗi đăng ký.")}
    except Exception as e:
        return {"success": False, "message": str(e)}

def get_history(session_id):
    try:
        resp = requests.get(f"{API_URL}/analyze/history", params={"session_id": session_id})
        if resp.status_code == 200:
            return resp.json().get("history", [])
        return []
    except Exception:
        return []
