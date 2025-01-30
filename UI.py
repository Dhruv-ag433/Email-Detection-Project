import streamlit as st
import requests

st.title("Email Phishing Detector")

subject = st.text_input("Enter Email Subject")
body = st.text_area("Enter Email Body")

if st.button("Predict"):
    
    response = requests.post("http://127.0.0.1:8000/predict", json = {"subject": subject, "body": body})
    result = response.json()
    st.write(f"Prediction: {result['Prediction']}")
    
    