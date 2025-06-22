from pydantic import BaseModel

class TextInput(BaseModel):
    text: str
    session_id: str = None
    conversation_id: int = None  # Kiểu int vì đó là id trong DB
    
