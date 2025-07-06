from flask import Flask, request, jsonify
import joblib
import numpy as np
import os
from sklearn.base import ClassifierMixin, RegressorMixin

app = Flask(__name__)

# Load the model once when the app starts
MODEL_PATH = "trained_model.pkl"  # replace with your actual model path
model = joblib.load(MODEL_PATH)

# Auto-detect model type (classifier or regressor)
if isinstance(model, ClassifierMixin):
    model_type = "classification"
elif isinstance(model, RegressorMixin):
    model_type = "regression"
else:
    raise ValueError("Unsupported model type loaded.")

@app.route('/')
def index():
    return "✅ ML Model API is Running"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.get_json()
        features = input_data.get("features", None)

        if features is None:
            return jsonify({"error": "Missing 'features' in request body"}), 400

        # Ensure input is 2D array
        features_array = np.array(features).reshape(1, -1) if isinstance(features[0], (int, float)) else np.array(features)

        predictions = model.predict(features_array)

        response = {
            "model_type": model_type,
            "predictions": predictions.tolist()
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
