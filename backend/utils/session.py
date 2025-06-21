import uuid

session_store = {}

def create_session(user_info: dict) -> str:
    session_id = str(uuid.uuid4())
    session_store[session_id] = user_info
    return session_id

def get_user_by_session(session_id: str):
    return session_store.get(session_id)

def delete_session(session_id: str):
    session_store.pop(session_id, None)
