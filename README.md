```markdown
# 📘 Vietnamese Text Readability Prediction

Một ứng dụng Machine Learning dùng mô hình BERT (PhoBERT) để phân loại độ khó văn bản tiếng Việt.  
Giao diện frontend được xây dựng bằng **Streamlit**, backend API sử dụng **FastAPI**.

---
```
## 📁 Cấu trúc thư mục

```

Vietnamese-Text-Readability/
├── backend/                 # FastAPI backend
│   ├── main.py
│   ├── routes/
│   ├── utils/
│   └── database/           # SQLite file chat\_history.db
├── frontend/               # Streamlit app
│   └── app.py
├── requirements.txt        # Python dependencies
├── Dockerfile              # Dùng chung cho cả BE & FE
├── docker-compose.yml      # Dựng cả 2 services
├── download\_model.py       # Tự tải model từ Google Drive nếu chưa có
├── readibility\_model.pt    # (file này được tải tự động, không cần push)
└── README.md               # File bạn đang đọc

````

---

## 🚀 Cách chạy (có 2 cách)

### ▶️ 1. DÙNG DOCKER (đề xuất)

> ⚠️ Yêu cầu: đã cài [Docker](https://www.docker.com/) + [Docker Compose](https://docs.docker.com/compose/)

```bash
# Tải model từ Google Drive nếu chưa có
# Build cả backend và frontend
docker-compose up --build
````

Mở trình duyệt:

* 📦 API: [http://localhost:8000/docs](http://localhost:8000/docs)
* 💻 Giao diện: [http://localhost:8501](http://localhost:8501)

📌 Mặc định model `readibility_model.pt` sẽ tự được tải từ Google Drive.

---

### 🛠️ 2. CHẠY LOCAL (không dùng Docker)

> ⚠️ Yêu cầu: Python 3.10+, pip

```bash
# Cài thư viện
pip install -r requirements.txt

# Tải model nếu chưa có
python download_model.py

# Chạy backend (API)
uvicorn backend.main:app --reload

# Chạy frontend (giao diện Streamlit) – tab mới
streamlit run frontend/app.py
```

---

## 🔎 API endpoint

Bạn có thể thử API tại: `http://localhost:8000/docs`

### POST `/analyze`

```json
{
  "text": "Văn bản cần đánh giá..."
}
```

---

## 🧠 Mô hình học máy

* Sử dụng pretrained `vinai/phobert-base`
* Fine-tuned trên tập dữ liệu readability tiếng Việt (tự xây dựng)
* Output: 1 trong 4 nhãn độ khó:

  * Dễ đọc
  * Trung bình
  * Khó đọc
  * Rất khó đọc

📦 File model `readibility_model.pt` (\~500MB) được lưu trên Google Drive và tự động tải khi chạy lần đầu.

---

## 👥 Thành viên nhóm

* 💻 \[Võ Nguyễn Song Huy, Nguyễn Hùng Việt] – BE, ML
* 🎨 \[Mai Nhựt Huy, Vy Quốc Huy] – FE, UI
* 📊 \[Trần Mạnh Hùng] – Dataset, Training

---

## 📝 Ghi chú

* Nếu gặp lỗi `connection refused`, kiểm tra xem backend đã khởi động chưa.
* File `chat_history.db` được mount từ host, đảm bảo tồn tại tại `backend/database/chat_history.db`.

---
