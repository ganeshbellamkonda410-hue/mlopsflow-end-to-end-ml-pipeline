import joblib
import pandas as pd
from pipelines.config import MODEL_PATH, FEATURE_COLUMNS

def build_features(payload: dict) -> pd.DataFrame:
    attendance = payload["attendance"]
    assignments_completed = payload["assignments_completed"]
    exam_score = payload["exam_score"]
    engagement_score = payload["engagement_score"]

    row = {
        "attendance": attendance,
        "assignments_completed": assignments_completed,
        "exam_score": exam_score,
        "engagement_score": engagement_score,
        "attendance_risk": 100 - attendance,
        "academic_risk": ((10 - assignments_completed) * 10 + (100 - exam_score)) / 2,
        "engagement_risk": 100 - engagement_score,
    }
    return pd.DataFrame([row])[FEATURE_COLUMNS]

def predict_dropout(payload: dict):
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Trained model not found. Run: python -m pipelines.run_pipeline")

    model = joblib.load(MODEL_PATH)
    features = build_features(payload)
    probability = float(model.predict_proba(features)[0][1])

    if probability >= 0.70:
        risk = "High"
    elif probability >= 0.40:
        risk = "Medium"
    else:
        risk = "Low"

    return {
        "dropout_risk": risk,
        "confidence": round(max(probability, 1 - probability), 4),
        "risk_probability": round(probability, 4),
    }
