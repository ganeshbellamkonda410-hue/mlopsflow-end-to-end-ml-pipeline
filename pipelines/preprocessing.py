import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # In this sample dataset, all values are numeric. This function is ready for adding encoders/scalers.
    numeric_cols = ["attendance", "assignments_completed", "exam_score", "engagement_score"]
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    print("[Preprocessing] Missing values handled.")
    return df
