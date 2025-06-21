# backend/main.py
from fastapi import FastAPI
from backend.utils.db import init_db
from backend.routes import login, register, analyze


init_db()

app = FastAPI(title="Vietnamese Readability API")
app.include_router(register.router)
app.include_router(login.router)
app.include_router(analyze.router)