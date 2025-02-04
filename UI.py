import streamlit as st
import requests

FASTAPI_URL = "http://localhost:8000/fetch-emails"

st.title("Email Fraud Detection")

st.write("Click the button below to fetch and classify your latest emails.")

if st.button("Fetch Emails"):
    with st.spinner("Fetching and Analyzing emails..."):
        response = requests.get(FASTAPI_URL)
        
        if response.status_code == 200:
            data = response.json()
            emails = data.get("Emails", [])
            
            if not emails:
                st.success("No new Emails found.")
            else:
                for email in emails:
                    st.subheader(f"From: {email['From']}")
                    st.write(f"Subject: {email['Subject']}")
                    st.write(f"Preview: {email['Body']}")
                    st.write(f"Phishing: {email['Phishing']}")
                    st.write(f"Spam: {email['Spam']}")
                    st.write(f"Phishing Prob: {email['Phishing_prob']}")
                    st.write(f"Spam Prob: {email['Spam_prob']}")
                    st.write("---")
        else:
            st.error("Error fetching emails. Please check the API connection.")

st.write("Refresh the page to check for new emails.")