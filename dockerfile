# ------------ BASE IMAGE ------------
FROM python:3.10-slim AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy script tải model
COPY download_model.py .

# ------------ BACKEND IMAGE ------------
FROM base AS backend
WORKDIR /app
COPY backend/ ./backend

# Tải model từ Google Drive
RUN python download_model.py

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# ------------ FRONTEND IMAGE ------------
FROM base AS frontend
WORKDIR /app
COPY frontend/ ./frontend
CMD ["streamlit", "run", "frontend/app.py", "--server.address=0.0.0.0", "--server.port=8501"]

# ------------ Database IMAGE ------------