# BE/models/auth.py
from pydantic import BaseModel, EmailStr

class RegisterInput(BaseModel):
    username: EmailStr
    full_name: str
    password: str
    

class LoginInput(BaseModel):
    username: str # = Email
    password: str
    
class LogoutInput(BaseModel):
    session_id: str