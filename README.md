# 💳 Credit Card Fraud Detection System (AI/ML)

## 📌 Overview
This project builds a machine learning system to detect fraudulent credit card transactions.  
It uses a **multi-layer approach** combining:
- Machine Learning (LightGBM)
- Rule-based checks
- Anomaly detection (Isolation Forest)

---

## 🚀 Features
- Detects fraud in real-time
- Uses multiple security layers
- Handles imbalanced data (SMOTE)
- Provides probability-based prediction
- Automatic time detection (IST)

---

## 🛠️ Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- LightGBM
- SHAP
- Matplotlib
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

```
Credit-Card-Fraud-Detection/
│
├── app.py
├── model.py
├── encoder.pkl
├── scaler.pkl
├── requirements.txt
│
├── static/
│   ├── bg credit.png
│   ├── credit-card-bg.mp4
│   ├── script.js
│   └── style.css
│
├── templates/
│   ├── index.html
│   └── login.html
│
└── .env   # (not uploaded to GitHub)
```
    
---

## ⚙️ Installation
Install dependencies:

```bash
pip install pandas numpy scikit-learn lightgbm shap matplotlib imbalanced-learn
