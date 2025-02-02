import joblib
import requests
from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

MODEL_URL = "https://huggingface.co/Dhruv-ag433/email-phishing-detection/blob/main/phishing_model.pkl"
VECTORIZER_URL ="https://huggingface.co/Dhruv-ag433/email-phishing-detection/blob/main/phishing_vectorizer.pkl" 

MODEL_FILE = "phishing_model.pkl"
VECTORIZER_FILE = "phishing_vectorizer.pkl"

def download_file(url, file_path):
    if not os.path.exists(file_path):
        print(f"Downloading {file_path} from {url}...")
        response = requests.get(url)
        with open(file_path, "wb") as f:
            f.write(response.content)
            
download_file(MODEL_URL, MODEL_FILE)
download_file(VECTORIZER_URL, VECTORIZER_FILE)

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
    
