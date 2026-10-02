import pandas as pd

REQUIRED_COLUMNS = {
    "student_id",
    "attendance",
    "assignments_completed",
    "exam_score",
    "engagement_score",
    "dropout",
}

def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    df = df.drop_duplicates(subset=["student_id"]).copy()

    numeric_cols = ["attendance", "assignments_completed", "exam_score", "engagement_score", "dropout"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    if df[numeric_cols].isnull().any().any():
        raise ValueError("Dataset contains null or non-numeric values after validation.")

    df["attendance"] = df["attendance"].clip(0, 100)
    df["assignments_completed"] = df["assignments_completed"].clip(0, 10)
    df["exam_score"] = df["exam_score"].clip(0, 100)
    df["engagement_score"] = df["engagement_score"].clip(0, 100)
    df["dropout"] = df["dropout"].astype(int).clip(0, 1)

    print("[Data Validation] Validation completed successfully.")
    return df
