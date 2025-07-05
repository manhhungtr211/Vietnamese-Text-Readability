import os
import torch
import torch.nn as nn
from transformers import AutoTokenizer

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
MODEL_PATH = os.path.join(BASE_DIR, "readibility_model.pt")

# --- 1. Định nghĩa lại class ReadibilityModel ---
class ReadibilityModel(nn.Module):
    def __init__(self, n_classes):
        super(ReadibilityModel, self).__init__()
        # load backbone PhoBERT
        from transformers import AutoModel
        self.bert = AutoModel.from_pretrained("vinai/phobert-base")
        self.drop = nn.Dropout(p=0.2)
        self.fc   = nn.Linear(self.bert.config.hidden_size, n_classes)
        # init weights
        nn.init.normal_(self.fc.weight, std=0.02)
        nn.init.normal_(self.fc.bias,   0)

    def forward(self, **batch):
        # output = (last_hidden_state, pooler_output)
        _, pooled = self.bert(**batch, return_dict=False)
        x = self.drop(pooled)
        return self.fc(x)    # trả về logits trực tiếp

# --- 2. Load tokenizer + model mới từ file readibility_model.pt ---
tokenizer = AutoTokenizer.from_pretrained("vinai/phobert-base", use_fast=False)

model = ReadibilityModel(n_classes=4)
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Không tìm thấy model tại {MODEL_PATH}")
model.load_state_dict(torch.load(MODEL_PATH, map_location="cpu"))
model.eval()

# Nhãn giữ nguyên
LABELS = ["Dễ đọc", "Trung bình", "Khó đọc", "Rất khó đọc"]

# --- 3. Hàm analyze_text không đổi tên, chỉ sửa bên trong để dùng model mới ---
def analyze_text(text: str):
    try:
        # tokenize như cũ
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            # model mới trả về logits chứ không phải outputs.logits
            logits = model(**inputs)

        # lấy dự đoán
        predicted_class_id = torch.argmax(logits, dim=1).item()
        probs = torch.softmax(logits, dim=1)
        confidence = probs[0][predicted_class_id].item()

        return {
            "predicted_class": predicted_class_id,
            "label":      LABELS[predicted_class_id],
            "confidence": round(confidence, 4),
            "difficulty": LABELS[predicted_class_id]
        }
    except Exception as e:
        return {"error": str(e)}
