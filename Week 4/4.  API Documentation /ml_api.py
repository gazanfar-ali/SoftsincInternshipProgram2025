pip install fastapi uvicorn scikit-learn joblib numpy

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib
from sklearn.base import ClassifierMixin, RegressorMixin

app = FastAPI(title="ML Model Prediction API", description="API that serves both classification and regression models", version="1.0")

# Load model at startup
MODEL_PATH = "trained_model.pkl"
model = joblib.load(MODEL_PATH)

if isinstance(model, ClassifierMixin):
    model_type = "classification"
elif isinstance(model, RegressorMixin):
    model_type = "regression"
else:
    raise ValueError("❌ Unsupported model type loaded.")

# Input schema using Pydantic
class InputData(BaseModel):
    features: list

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "✅ ML Model API is Running", "model_type": model_type}

@app.post("/predict", tags=["Prediction"])
def predict(data: InputData):
    try:
        features = data.features

        # Ensure features is a 2D array
        features_array = np.array(features).reshape(1, -1) if isinstance(features[0], (int, float)) else np.array(features)

        predictions = model.predict(features_array).tolist()

        return {
            "model_type": model_type,
            "predictions": predictions
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
