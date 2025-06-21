import sqlite3
import os

DB_PATH = "database/chat_history.db"

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

    # Tạo bảng CHAT_HISTORY
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CHAT_HISTORY (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            message TEXT NOT NULL,
            reply TEXT,
            error TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES USER(user_id)
        )
    """)

    conn.commit()
    conn.close()
    print(f"✅ DB initialized at {DB_PATH}")
