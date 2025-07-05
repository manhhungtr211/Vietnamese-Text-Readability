# FE/config.py
# Configuration file for frontend settings.
import os
# URL của FastAPI backend
API_URL = os.getenv("API_BASE_URL", "http://localhost:8000")