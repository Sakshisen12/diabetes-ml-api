# Diabetes Prediction ML API 🩺

A machine learning based REST API to predict whether a person is diabetic.

## Tech Stack
- Python
- FastAPI
- Scikit-learn
- NumPy

## API Endpoint
POST /predict

## Sample Request
```json
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
Response
{
  "prediction": "Diabetic"
}