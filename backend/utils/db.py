import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "database", "chat_history.db")
DB_PATH = os.path.abspath(DB_PATH)

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)  # ← tạo thư mục nếu chưa có

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Tạo bảng USER
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS USER (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            full_name TEXT NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Tạo bảng CONVERSATION
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CONVERSATION (
            conversation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            title TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES USER(user_id)
        )
    """)

    # Tạo bảng CHAT_HISTORY (liên kết với CONVERSATION, không còn user_id)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CHAT_HISTORY (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            conversation_id INTEGER NOT NULL,
            message TEXT NOT NULL,
            reply TEXT,
            error TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(conversation_id) REFERENCES CONVERSATION(conversation_id)
        )
    """)

    conn.commit()
    conn.close()
    print(f"connected to database successfully")
