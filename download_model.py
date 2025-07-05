# download_model.py
import os
import gdown

MODEL_PATH = "readibility_model.pt"
GDRIVE_ID = "1SS6fvKCFnoxPQwAQ8xv-J_wibMHdj-iG" 
URL = f"https://drive.google.com/uc?id={GDRIVE_ID}"

if not os.path.exists(MODEL_PATH):
    print(f"[INFO] Downloading model from Google Drive...")
    gdown.download(URL, MODEL_PATH, quiet=False)
else:
    print(f"[INFO] Model already exists: {MODEL_PATH}")
