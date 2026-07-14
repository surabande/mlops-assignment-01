from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import os

# Initialize FastAPI app
app = FastAPI(title="Heart Disease Prediction API", description="MLOps Assignment 01 API")

# Define the path to the model and load it
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../src/best_model.pkl")

try:
    model_pipeline = joblib.load(MODEL_PATH)
except Exception as e:
    model_pipeline = None
    print(f"Error loading model: {e}")

# Define the expected JSON input schema using Pydantic
class PatientData(BaseModel):
    age: float
    sex: float
    cp: float
    trestbps: float
    chol: float
    fbs: float
    restecg: float
    thalach: float
    exang: float
    oldpeak: float
    slope: float
    ca: float
    thal: float

@app.get("/")
def home():
    return {"message": "Welcome to the Heart Disease Prediction API. Use the /predict endpoint."}

@app.post("/predict")
def predict(data: PatientData):
    if model_pipeline is None:
        raise HTTPException(status_code=500, detail="Model is not loaded.")
    
    # Convert incoming JSON data to a Pandas DataFrame
    input_data = pd.DataFrame([data.dict()])
    
    try:
        # Generate prediction and confidence score
        prediction = model_pipeline.predict(input_data)[0]
        probability = model_pipeline.predict_proba(input_data)[0].tolist()
        
        # Map prediction to human-readable label
        result_label = "Disease Present" if prediction == 1 else "No Disease"
        
        # Return prediction and confidence/probability score as required by the assignment
        return {
            "prediction": int(prediction),
            "label": result_label,
            "confidence_scores": {
                "No Disease": probability[0],
                "Disease Present": probability[1]
            }
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))