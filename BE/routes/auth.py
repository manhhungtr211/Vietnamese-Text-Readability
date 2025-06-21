# backend/routes/auth.py
from fastapi import APIRouter
from models.login import LoginInput, RegisterInput
import json
import os
from typing import Dict

router = APIRouter()
DB_PATH = os.path.join(os.path.dirname(__file__), '../db/users.json')

def load_users() -> Dict[str, str]:
    if not os.path.exists(DB_PATH):
        return {}
    with open(DB_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_users(users: Dict[str, str]):
    with open(DB_PATH, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

@router.post("/login")
def login(data: LoginInput):
    users = load_users()
    if data.username in users and users[data.username] == data.password:
        return {"success": True}
    return {"success": False}

@router.post("/register")
def register(data: RegisterInput):
    users = load_users()
    if data.username in users:
        return {"success": False}
    users[data.username] = data.password
    save_users(users)
    return {"success": True}
