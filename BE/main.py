# backend/main.py
from fastapi import FastAPI
from routes import auth, analyze

app = FastAPI(title="Vietnamese Readability API")
app.include_router(auth.router)
app.include_router(analyze.router)
