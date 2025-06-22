from fastapi import APIRouter, HTTPException
from backend.utils.session import get_user_id_by_session
from backend.utils.db import execute_query
from pydantic import BaseModel

router = APIRouter()

class ConversationRequest(BaseModel): # cần tổ chức lại các model cho gọn
    conversation_id: int
    
@router.post("/conversation_detail")
def get_conversation_detail(data: ConversationRequest):
    try:
        query = """
            SELECT message, reply, created_at 
            FROM CHAT_HISTORY 
            WHERE conversation_id = ? 
            ORDER BY created_at ASC
        """
        results = execute_query(query, (data.conversation_id,))

        return {
            "conversation_id": data.conversation_id,
            "messages": [
                {
                    "message": row[0],
                    "reply": row[1],
                    "created_at": row[2]
                } for row in results
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving conversation details: {str(e)}")