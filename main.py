from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib

# Create FastAPI app
app = FastAPI(title="Heart Disease Prediction API")

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained model
model = joblib.load("heart_model.pkl")


# Test API
@app.get("/")
def home():
    return {
        "message": "Heart Disease Prediction API is running"
    }


# Prediction API
@app.post("/predict")
def predict(data: dict):

    features = [[
        data["age"],
        data["sex"],
        data["cp"],
        data["trestbps"],
        data["chol"],
        data["fbs"],
        data["restecg"],
        data["thalach"],
        data["exang"],
        data["oldpeak"],
        data["slope"],
        data["ca"],
        data["thal"]
    ]]

    # Make prediction
    prediction = model.predict(features)[0]

    # Convert prediction to readable result
    if prediction == 1:
        result = "Heart Disease Detected"
    else:
        result = "No Heart Disease Detected"

    return {
        "prediction": int(prediction),
        "result": result
    }