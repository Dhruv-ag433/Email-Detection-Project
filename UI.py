import streamlit as st
import requests

FASTAPI_URL = http://onrender.com

st.title("Email Phishing Detector")

subject = st.text_input("Enter Email Subject")
body = st.text_area("Enter Email Body")

if st.button("Predict"):
    
    response = requests.post(FASTAPI_URL, json = {"subject": subject, "body": body})
    result = response.json()
    st.write(f"Prediction: {result['Prediction']}")
    
    
