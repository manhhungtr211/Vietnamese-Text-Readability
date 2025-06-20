from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Đường dẫn tới model đã fine-tuned
model_path = r"C:\Workspace\ML\DA\checkpoint-3000\checkpoint-3000"

# Load tokenizer và model
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

print("✅ Model loaded successfully!")
print("Nhập 'exit' để thoát chương trình.")

# Vòng lặp nhập liệu
while True:
    text = input("\n👉 Nhập câu tiếng Việt để phân tích: ")
    
    if text.lower().strip() == "exit":
        print("👋 Kết thúc chương trình.")
        break

    # Tiền xử lý và dự đoán
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)

    # Lấy kết quả phân loại
    logits = outputs.logits
    predicted_class_id = torch.argmax(logits, dim=1).item()

    print(f"🔎 Kết quả dự đoán: lớp {predicted_class_id}")
