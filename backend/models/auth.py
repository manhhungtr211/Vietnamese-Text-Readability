# BE/models/auth.py
from pydantic import BaseModel, EmailStr

class RegisterInput(BaseModel):
    username: EmailStr
    full_name: str
    password: str
    

class LoginInput(BaseModel):
    username: str
    password: str

class TextInput(BaseModel):
    text: str

class HistoryInput(BaseModel):
    username: str
