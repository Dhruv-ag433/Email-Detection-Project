from googleapiclient.discovery import build
from auth import authenticate_gmail
import requests
import base64
import pickle
import re
import os

#URLs for the Models and Vectorizers
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

#Load the Models and Vectorizers
with open(PHISHING_MODEL_FILE, 'rb') as model_file:
    phishing_model = pickle.load(model_file)
    
with open(PHISHING_VECTORIZER_FILE, 'rb') as vectorizer_file:
    phishing_vectorizer = pickle.load(vectorizer_file)
    
with open(SPAM_MODEL_FILE, 'rb') as model_file:
    spam_model = pickle.load(model_file)
    
with open(SPAM_VECTORIZER_FILE, 'rb') as vectorizer_file:
    spam_vectorizer = pickle.load(vectorizer_file)
    
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

def classify_email(text):
    input_text = preprocess_text(text)
    
    #Phishing Prediction
    phishing_input_vector = phishing_vectorizer.transform([input_text])
    phishing_probs = phishing_model.predict_proba(phishing_input_vector).tolist()
    
    #Spam Prediction
    spam_input_vector = spam_vectorizer.transform([input_text])
    spam_probs = spam_model.predict_proba(spam_input_vector).tolist()
    
    phishing_threshold = 0.55
    spam_threshold = 0.6
    return {
        "Phishing": "Yes" if phishing_probs[0][1] >= phishing_threshold else "No",
        "Spam": "Yes" if spam_probs[0][1] >= spam_threshold else "No"
    }
    
def get_recent_emails():
    creds = authenticate_gmail()
    service = build('gmail', 'v1', credentials = creds)
    
    results = service.users().messages().list(userId='me', maxResults=5).execute()
    messages = results.get('messages', [])
    
    if not messages:
        print("No new E-mails found.")
        return
    
    email_results = []
    for msg in messages:
        msg_id = msg['id']
        msg_data = service.users().messages().get(userId='me', id=msg_id).execute()
        
        payload = msg_data['payload']
        headers = payload['headers']
        
        subject = None
        sender = None
        body = None
        
        for header in headers:
            if header['name'] == 'Subject':
                subject = header['value']
            if header['name'] == 'From':
                sender = header['value']
                
        if 'parts' in payload:
            for part in payload['parts']:
                if part['mimeType'] == 'text/plain':
                    if 'data' in part['body']:
                        body = base64.urlsafe_b64decode(part['body']['data']).decode(errors='ignore')
                    break
                    
        elif 'body' in payload and 'data' in payload['body']:
            body = base64.urlsafe_b64decode(payload['body']['data']).decode(errors='ignore')
        
        if body:
            classify = classify_email(body)
        
            email_info = {
                "From": sender,
                "Subject": subject,
                "Body": body[:200],
                "Phishing": classify["Phishing"],
                "Spam": classify["Spam"]
            }
            email_results.append(email_info)
        
            print(f"From: {sender}\nSubject: {subject}\nBody: {body[:200]}\n---\n")
        else:
            print(f"Email from {sender} does not contain a body.")
    
    return email_results
    
if __name__ == '__main__':
    get_recent_emails()