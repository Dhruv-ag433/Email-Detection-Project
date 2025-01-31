import streamlit as st
import requests

FASTAPI_URL = "http://localhost:8000/predict"

st.title("Email Phishing Detector")

subject = st.text_input("Enter Email Subject")
body = st.text_area("Enter Email Body")

if st.button("Predict"):
    if subject and body:
        response = requests.post(FASTAPI_URL, json = {"subject": subject, "body": body})
        if response.status_code == 200:
            result = response.json()
            st.write(f"Prediction: {result['Prediction']}")
        else:
            st.error("Error in prediction request")
    
    else:
        st.error("Please provide both subject and body of the email.")
    