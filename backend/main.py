# backend/main.py
from fastapi import FastAPI
from backend.utils.db import init_db
from backend.routes import login, register, analyze, logout, conversation, conversation_detail


init_db()

app = FastAPI(title="Vietnamese Readability API")
app.include_router(register.router)
app.include_router(login.router)
app.include_router(analyze.router)
app.include_router(logout.router)
app.include_router(conversation.router)
app.include_router(conversation_detail.router)