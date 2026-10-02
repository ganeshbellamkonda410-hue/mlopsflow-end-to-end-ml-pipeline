from pipelines.config import PROCESSED_DATA_PATH
from pipelines.data_ingestion import load_data
from pipelines.data_validation import validate_data
from pipelines.preprocessing import preprocess_data
from pipelines.feature_engineering import create_features
from pipelines.model_training import train_model

def run_pipeline():
    df = load_data()
    df = validate_data(df)
    df = preprocess_data(df)
    df = create_features(df)

    PROCESSED_DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"[Pipeline] Processed data saved to {PROCESSED_DATA_PATH}")

    model, metrics = train_model(df)
    print("[Pipeline] Pipeline completed successfully.")
    return model, metrics

if __name__ == "__main__":
    run_pipeline()
