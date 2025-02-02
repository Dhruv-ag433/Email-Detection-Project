import pickle
import requests
from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

#URLs for the models and vectorizers
PHISHING_MODEL_URL = "https://huggingface.co/Dhruv-ag433/Email_Detection_Models/resolve/main/phishing_model.pkl"
PHISHING_VECTORIZER_URL ="https://huggingface.co/Dhruv-ag433/Email_Detection_Models/resolve/main/phishing_vectorizer.pkl"
SPAM_MODEL_URL = "https://huggingface.co/Dhruv-ag433/Email_Detection_Models/resolve/main/spam_model.pkl"
SPAM_VECTORIZER_URL = "https://huggingface.co/Dhruv-ag433/Email_Detection_Models/resolve/main/spam_vectorizer.pkl" 

#File paths for the saved models and vectorizers
PHISHING_MODEL_FILE = "phishing_model.pkl"
PHISHING_VECTORIZER_FILE = "phishing_vectorizer.pkl"
SPAM_MODEL_FILE = "spam_model.pkl"
SPAM_VECTORIZER_FILE = "spam_vectorizer.pkl"

def download_file(url, file_path):
    if not os.path.exists(file_path):
        print(f"Downloading {file_path} from {url}...")
        response = requests.get(url)
        with open(file_path, "wb") as f:
            f.write(response.content)
          
download_file(PHISHING_MODEL_URL, PHISHING_MODEL_FILE)
download_file(PHISHING_VECTORIZER_URL, PHISHING_VECTORIZER_FILE)
download_file(SPAM_MODEL_URL, SPAM_MODEL_FILE)
download_file(SPAM_VECTORIZER_URL, SPAM_VECTORIZER_FILE)

#Load the models and vectorizers
with open(PHISHING_MODEL_FILE, 'rb') as model_file:
    phishing_model = pickle.load(model_file)
    
with open(PHISHING_VECTORIZER_FILE, 'rb') as vectorizer_file:
    phishing_vectorizer = pickle.load(vectorizer_file)
    
with open(SPAM_MODEL_FILE, 'rb') as model_file:
    spam_model = pickle.load(model_file)
    
with open(SPAM_VECTORIZER_FILE, 'rb') as vectorizer_file:
    spam_vectorizer = pickle.load(vectorizer_file)
    
class EmailData(BaseModel):
    subject: str
    body: str
    
@app.get("/")
def read_root():
    return {"message": "Hello, World"}
    
@app.post("/predict")
def predict(email: EmailData):
    
    input_text = email.subject + " " + email.body
    
    #Phishing Prediction
    phishing_input_vector = phishing_vectorizer.transform([input_text])
    phishing_prediction = phishing_model.predict(phishing_input_vector)
    phishing_label = "Phishing" if phishing_prediction[0] == 1 else "Safe"
    
    #Spam Prediction
    spam_input_vector = spam_vectorizer.transform([input_text])
    spam_prediction = spam_model.predict(spam_input_vector)
    spam_label = "Spam" if spam_prediction[0] == 1 else "Ham"
    
    return {
        "Phishing Prediction": phishing_label,
        "Spam Prediction": spam_label
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host = "0.0.0.0", port = 8000)
    
