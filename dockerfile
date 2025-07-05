# ------------ BASE IMAGE ------------
FROM python:3.10-slim AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# ------------ BACKEND IMAGE ------------
FROM base AS backend
WORKDIR /app
COPY backend/ ./backend
COPY readibility_model.pt ./readibility_model.pt
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


# ------------ FRONTEND IMAGE ------------
FROM base AS frontend
WORKDIR /app
COPY frontend/ ./frontend
CMD ["streamlit", "run", "frontend/app.py", "--server.address=0.0.0.0", "--server.port=8501"]
