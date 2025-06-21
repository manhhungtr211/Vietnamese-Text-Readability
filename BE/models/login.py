# backend/models/login.py
from pydantic import BaseModel

class LoginInput(BaseModel):
    username: str
    password: str

class RegisterInput(BaseModel):
    username: str
    password: str

class TextInput(BaseModel):
    text: str

class HistoryInput(BaseModel):
    username: str
