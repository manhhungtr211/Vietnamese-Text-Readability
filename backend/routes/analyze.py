from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.utils.model import analyze_text
from backend.utils.session import get_user_by_session
import sqlite3, os

router = APIRouter()
DB_PATH = os.path.join(os.path.dirname(__file__), '../database/chat_history.db')

class TextInput(BaseModel):
    text: str
    session_id: str = None
    conversation_id: int = None  # Kiểu int vì đó là id trong DB

@router.post("/analyze")
def handle_analyze(input_data: TextInput):
    result = analyze_text(input_data.text)

    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])

    # Nếu có session thì xử lý lưu lịch sử
    if input_data.session_id:
        user = get_user_by_session(input_data.session_id)
        if user:
            try:
                conn = sqlite3.connect(DB_PATH)
                cursor = conn.cursor()

                # Nếu có conversation_id thì dùng luôn
                conversation_id = input_data.conversation_id

                # Nếu chưa có conversation_id thì tạo mới
                if not conversation_id:
                    cursor.execute("""
                        INSERT INTO CONVERSATION (user_id, title)
                        VALUES (?, ?)
                    """, (user["user_id"], input_data.text[:50])) # lấy 50 ký tự đầu tiên làm tiêu đề
                    conversation_id = cursor.lastrowid

                # Ghi lịch sử
                cursor.execute("""
                    INSERT INTO CHAT_HISTORY (conversation_id, message, reply)
                    VALUES (?, ?, ?)
                """, (conversation_id, input_data.text, result["label"]))

                conn.commit()
                conn.close()

                # Gửi lại conversation_id cho FE biết để dùng tiếp lần sau
                result["conversation_id"] = conversation_id

            except Exception as e:
                print(f"Lỗi khi lưu lịch sử: {e}")

    return result
