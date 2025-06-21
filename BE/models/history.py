from pydantic import BaseModel

class HistoryInput(BaseModel):
    username: str
