from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

class ModelInput(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

# Load model
diabetes_model = pickle.load(open("trained_model(2).sav", "rb"))

@app.post("/diabetes_prediction")
def diabetes_prediction(input_data: ModelInput):

    input_list = [
        input_data.Pregnancies,
        input_data.Glucose,
        input_data.BloodPressure,
        input_data.SkinThickness,
        input_data.Insulin,
        input_data.BMI,
        input_data.DiabetesPedigreeFunction,
        input_data.Age
    ]

    prediction = diabetes_model.predict(np.array([input_list]))

    if prediction[0] == 0:
        result = "Not Diabetic"
    else:
        result = "Diabetic"

    return {"prediction": result}
