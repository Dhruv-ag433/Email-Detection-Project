
# 📧 Email Fraud Detection System

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Backend-FastAPI-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red?logo=streamlit)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

An intelligent system that uses machine learning to detect and classify **phishing** and **spam** emails from your Gmail inbox in real-time.

---

## 🚀 Project Overview

Email fraud — including phishing and spam — continues to be one of the most common online threats. This project is a full-stack **Email Fraud Detection System** that:
- Authenticates users via **Google OAuth**
- Fetches their recent emails using the **Gmail API**
- Classifies them as **Phishing** or **Spam** using trained ML models

The system is built with **FastAPI** (backend), **Streamlit** (frontend), and supports **real-time classification** using models hosted on Hugging Face.

---

## 🧠 Key Features

- 🔐 **Google OAuth 2.0 Authentication**  
  Securely sign in and grant access to your Gmail inbox

- 📬 **Gmail API Integration**  
  Automatically fetch recent emails from your Gmail account

- ⚡ **Real-time Email Classification**  
  Classify emails as:
  - `Phishing`: Malicious content intended to steal sensitive data
  - `Spam`: Unwanted promotional or bulk messages

- 🧑‍💻 **User-Friendly Interface**  
  Clean and interactive UI using Streamlit for seamless user experience

- 📦 **Model Hosting on Hugging Face**  
  Vectorizer and ML models are loaded from Hugging Face for faster deployment

---

## 🛠️ Tech Stack

| Area       | Tools / Libraries                                  |
|------------|----------------------------------------------------|
| Backend    | FastAPI, Uvicorn                                   |
| Frontend   | Streamlit                                          |
| ML Models  | Scikit-learn (Random Forest, Naive Bayes)          |
| OAuth      | Google OAuth 2.0                                   |
| API        | Gmail API                                          |
| Deployment | Docker (local), Hugging Face (model storage)       |
| Others     | Requests, Pandas, Pickle, JSON, dotenv             |

---

## 📁 Project Structure

```
email-fraud-detection/
│
├── app/                   # FastAPI backend
│   └── ...               
├── ui/                    # Streamlit frontend
│   └── ...
├── models/                # ML models (vectorizer, phishing, spam)
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── .env                   # Gmail API credentials and secrets
```

---

## 📦 Installation

### 🔧 Prerequisites
- Python 3.8+
- Gmail API credentials
- Virtual environment (optional but recommended)

### 📥 Clone the Repository
```bash
git clone https://github.com/your-username/email-fraud-detection.git
cd email-fraud-detection
```

### 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

### 🔑 Setup `.env`
Create a `.env` file with your Gmail API and OAuth credentials:
```env
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
REDIRECT_URI=http://localhost:8501
```

---

## ▶️ Run the App

### 🔹 Start FastAPI Backend
```bash
uvicorn app.main:app --reload
```

### 🔹 Start Streamlit Frontend
```bash
cd ui
streamlit run main.py
```

---

## 🧪 Sample Dataset

The models were trained on:
- Public phishing & spam datasets
- Preprocessed Gmail messages
- Feature extraction using `TfidfVectorizer`

---

## 🧠 Model Details

| Task         | Algorithm        |
|--------------|------------------|
| Phishing     | Random Forest    |
| Spam         | Multinomial Naive Bayes |

Trained models and vectorizers are hosted on Hugging Face for easy loading and reuse.

---

## 🐳 Docker (Optional)

Build and run with Docker:

```bash
docker build -t email-detector .
docker run -p 8501:8501 email-detector
```

---

## 📈 Future Scope

- ✅ Real-time detection
- ✅ Phishing detection
- ✅ Spam detection
- 🔄 Dataset Expansion
- 🌐 Live Deployment (Planned for local use only)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Dhruv Agarwal**  
📧 dhruv.agarwal433@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/dhruvagarwal433/)  

---

## 🌟 Show Your Support

If you found this project helpful, please ⭐ it and share it with others!
