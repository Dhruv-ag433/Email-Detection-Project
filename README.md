# Email Fraud Detection System

This project is an **Email Fraud Detection System** that classifies emails into **Phishing** and **Spam** categories using machine learning models. The system leverages Google's Gmail API to fetch recent emails and uses pre-trained classification models to detect whether an email is phishing or spam in real-time. The backend is built using **FastAPI**, while the frontend is designed with **Streamlit** for an interactive and user-friendly interface. The project also implements **Google OAuth** for secure authentication to access Gmail data.

## Project Description

The aim of this project is to build a system that can help users identify fraudulent or spam emails from their Gmail accounts. With the increasing number of phishing attacks and spam emails, a solution that can automatically classify these emails helps users stay protected and more informed. The system can classify incoming emails as:

- **Phishing**: Emails that are malicious, often intended to steal sensitive information such as passwords or credit card numbers.
- **Spam**: Unwanted emails, often promotional in nature, that can clutter the inbox.

The project is structured to authenticate the user via Google OAuth, fetch their recent emails from Gmail, and classify each email based on its content using pre-trained machine learning models. The user interface provides an intuitive way to view and interact with the results of email classification.

## Features

- **OAuth Authentication**: Allows users to authenticate with their Google account using OAuth and grant permission to access Gmail data.
- **Fetch Recent Emails**: Fetches recent emails from the user's Gmail account using the Gmail API.
- **Email Classification**: Classifies emails as **Phishing** or **Spam** using pre-trained models.
- **User Interface**: A simple and intuitive UI built with Streamlit for easy interaction.

## Technologies Used

- **Backend**: FastAPI (Python)
- **Frontend**: Streamlit (Python)
- **Google API**: Google Gmail API for fetching emails
- **Machine Learning**: Scikit-learn for the phishing and spam classification models
- **Authentication**: Google OAuth 2.0
- **Model Hosting**: HuggingFace (for model and vectorizer storage)

## Requirements

Before running the project, ensure that you have the following installed:

- Python 3.8 or higher
- Pip

You will also need to install the necessary dependencies:

```bash
pip install -r requirements.txt
