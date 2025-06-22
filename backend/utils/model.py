from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_path = r"D:\HuyMai\Y3-HK2\IntroToMachineLearning\Project\checkpoint-3000"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

LABELS = ["Dễ đọc", "Trung bình", "Khó đọc", "Rất khó đọc"]

def analyze_text(text: str):
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
            "difficulty": LABELS[predicted_class_id]
        }
    except Exception as e:
        return {"error": str(e)}
