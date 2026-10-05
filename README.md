# heart-disease-prediction-system
Machine learning based heart disease prediction system using Python, FastAPI and a web interface.
# Heart Disease Prediction System

A machine learning-based web application that predicts the possibility of heart disease based on a patient's medical information.

The project uses a Logistic Regression machine learning model with a FastAPI backend and a web-based frontend.

## 📌 Project Overview

Heart disease is one of the major health concerns worldwide. Early prediction can help identify individuals who may be at higher risk and encourage timely medical consultation.

This project takes important health-related parameters as input and uses a trained machine learning model to generate a prediction.

> **Disclaimer:** This project is developed for educational and demonstration purposes only. It is not intended to provide medical diagnosis or replace professional medical advice.

## ✨ Features

- User-friendly web interface
- Heart disease prediction using Machine Learning
- Logistic Regression model
- FastAPI backend
- REST API for prediction
- Real-time communication between frontend and backend
- JSON-based API requests and responses

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Logistic Regression
- Joblib

### Backend
- FastAPI
- Uvicorn

### Frontend
- HTML
- CSS
- JavaScript

## 📊 Input Features

The model uses the following 13 input features:

1. Age
2. Sex
3. Chest Pain Type (cp)
4. Resting Blood Pressure (trestbps)
5. Cholesterol (chol)
6. Fasting Blood Sugar (fbs)
7. Resting ECG (restecg)
8. Maximum Heart Rate (thalach)
9. Exercise-Induced Angina (exang)
10. ST Depression (oldpeak)
11. Slope
12. Number of Major Vessels (ca)
13. Thalassemia (thal)

## 🤖 Machine Learning Model

A Logistic Regression model was trained using a heart disease dataset.

The trained model is saved as:

```text
heart_model.pkl
