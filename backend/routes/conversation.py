from fastapi import APIRouter, HTTPException
from backend.utils.session import get_user_id_by_session
from backend.utils.db import execute_query
from pydantic import BaseModel

router = APIRouter()

class SessionRequest(BaseModel): # cần tổ chức lại các model cho gọn
    session_id: str

@router.post("/conversations")
def get_conversations(data: SessionRequest):
    user_id = get_user_id_by_session(data.session_id)

    if not user_id:
        raise HTTPException(status_code=404, detail="Session not found")

    query = """
        SELECT conversation_id, title, created_at 
        FROM CONVERSATION 
        WHERE user_id = ? 
        ORDER BY created_at DESC
    """
    results = execute_query(query, (user_id,))

    return {
        "conversations": [
            {
                "conversation_id": row[0],
                "title": row[1],
                "created_at": row[2]
            } for row in results
        ]
    }
