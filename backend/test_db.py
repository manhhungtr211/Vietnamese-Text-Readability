import sqlite3

conn = sqlite3.connect("backend/database/chat_history.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM USER")
rows = cursor.fetchall()
print("USER TABLE:")
for row in rows:
    print(row)

cursor.execute("SELECT * FROM CONVERSATION")
rows = cursor.fetchall()
print("\nCONVERSATION TABLE:")
for row in rows:
    print(row)

cursor.execute("SELECT * FROM CHAT_HISTORY")
rows = cursor.fetchall()
print("\nCHAT_HISTORY TABLE:")
for row in rows:
    print(row)

conn.close()
