from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_path = r"C:\Workspace\ML\DA\checkpoint-3000\checkpoint-3000"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

# Optional: định nghĩa nhãn nếu có
LABELS = ["Dễ đọc", "Trung bình", "Khó đọc", "Rất khó đọc"]


def analyze_text(text: str):
    """
    Phân tích độ khó văn bản bằng mô hình đã fine-tuned.

    Args:
        text (str): Văn bản tiếng Việt cần phân tích.

    Returns:
        dict: Kết quả phân loại (lớp, nhãn, xác suất).
    """
    try:
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = model(**inputs)

        logits = outputs.logits
        predicted_class_id = torch.argmax(logits, dim=1).item()
        confidence = torch.softmax(logits, dim=1)[0][predicted_class_id].item()

        return {
            "predicted_class": predicted_class_id,
            "label": LABELS[predicted_class_id] if predicted_class_id < len(LABELS) else f"Lớp {predicted_class_id}",
            "confidence": round(confidence, 4),
            "difficulty": LABELS[predicted_class_id]  # Thêm dòng này để tương thích UI cũ
        }
    except Exception as e:
        return {"error": str(e)}
