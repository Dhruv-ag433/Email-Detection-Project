import os
os.environ["KAGGLE_USERNAME"] = "dhruvagarwal433"
os.environ["KAGGLE_KEY"] = "2ed247573a84f0d2890fe164a168af53"
import kaggle
import pickle
import joblib
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

os.makedirs(os.path.expanduser("~/.kaggle"), exist_ok = True)

kaggle_json = {
    "username": "dhruvagarwal433",
    "key": os.getenv("KAGGLE_KEY")
}
with open(os.path.expanduser("~/.kaggle/kaggle.json"), "w") as kaggle_file:
    import json
    json.dump(kaggle_json, kaggle_file)
os.chmod(os.path.expanduser("~/.kaggle/kaggle.json"), 0o600)

KAGGLE_DATASET = "dhruvagarwal433/email_phishing_classifier"

MODEL_FILE = "phishing_email_classifier.pkl"
VECTORIZER_FILE = "vectorizer.pkl"

if not os.path.exists(MODEL_FILE) or not os.path.exists(VECTORIZER_FILE):
    kaggle.api.dataset_download_files(KAGGLE_DATASET, path = "./", unzip = True)

model = joblib.load(MODEL_FILE)
vectorizer = joblib.load(VECTORIZER_FILE)

class EmailData(BaseModel):
    subject: str
    body: str
    
@app.get("/")
def read_root():
    return {"message": "Hello, World"}
    
@app.post("/predict")
def predict(email: EmailData):
    
    input_text = email.subject + " " + email.body
    input_vector = vectorizer.transform([input_text])
    
    prediction = model.predict(input_vector)
    
    return {"Prediction": "Phishing" if prediction[0] == 1 else "Safe"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host = "0.0.0.0", port = 8000)
    
