# backend/main.py
from fastapi import FastAPI
from backend.utils.db import init_db
from backend.routes import auth

init_db()

app = FastAPI(title="Vietnamese Readability API")
app.include_router(auth.router)
#app.include_router(analyze.router)
