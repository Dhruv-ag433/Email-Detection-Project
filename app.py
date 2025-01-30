from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import joblib

app = FastAPI()

model = joblib.load('phishing_email_classifier.pkl')
vectorizer = joblib.load('vectorizer.pkl')

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
    