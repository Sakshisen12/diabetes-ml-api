🩺 Diabetes Prediction ML API

A machine learning–based REST API that predicts whether a person is diabetic using medical parameters.
The model is deployed as a public FastAPI service.

🚀 Tech Stack

Python

FastAPI

Scikit-learn

NumPy

Uvicorn

Render (Deployment)

🔗 Live API
https://diabetes-ml-api-7q1a.onrender.com


Swagger Docs:

/docs

📌 API Endpoint

POST /diabetes_prediction

📥 Sample Request
{
  "Pregnancies": 6,
  "Glucose": 148,
  "BloodPressure": 72,
  "SkinThickness": 35,
  "Insulin": 0,
  "BMI": 33.6,
  "DiabetesPedigreeFunction": 0.627,
  "Age": 50
}

📤 Sample Response
{
  "prediction": 1,
  "result": "Diabetic"
}


or

{
  "prediction": 0,
  "result": "Not Diabetic"
}

🧪 How to Test

Open /docs for interactive Swagger UI

Or send a POST request using Postman / Python requests

📌 Notes

This API uses a trained ML model (.sav) for inference

Designed for learning and demonstration purposes
