# FE/api.py
# Handles communication with the FastAPI backend.

import requests
from FE.config import API_URL

def analyze_text(text: str):
    """
    Send a POST request to the backend API to analyze the given text.

    Args:
        text (str): The Vietnamese text to analyze.

    Returns:
        dict: The response from the backend, or an error message.
    """
    try:
        response = requests.post(API_URL, json={"text": text})
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Lỗi: {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}
