import json
import joblib
import mlflow
import mlflow.sklearn
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from pipelines.config import FEATURE_COLUMNS, TARGET_COLUMN, MODEL_PATH, REPORT_PATH

def train_model(df: pd.DataFrame):
    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    params = {
        "n_estimators": 120,
        "max_depth": 4,
        "learning_rate": 0.08,
        "subsample": 0.9,
        "eval_metric": "logloss",
        "random_state": 42,
    }

    mlflow.set_experiment("student-dropout-risk-prediction")

    with mlflow.start_run(run_name="xgboost-dropout-risk-model"):
        model = XGBClassifier(**params)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)

        metrics = {
            "accuracy": float(accuracy_score(y_test, preds)),
            "precision": float(precision_score(y_test, preds, zero_division=0)),
            "recall": float(recall_score(y_test, preds, zero_division=0)),
            "f1_score": float(f1_score(y_test, preds, zero_division=0)),
        }

        mlflow.log_params(params)
        mlflow.log_metrics(metrics)
        mlflow.sklearn.log_model(model, artifact_path="model")

        MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(model, MODEL_PATH)

        REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
        REPORT_PATH.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

        print(f"[Model Training] Model saved to {MODEL_PATH}")
        print(f"[Model Training] Metrics: {metrics}")

    return model, metrics

if __name__ == "__main__":
    from pipelines.run_pipeline import run_pipeline
    run_pipeline()
