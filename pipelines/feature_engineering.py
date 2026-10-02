import pandas as pd

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["attendance_risk"] = 100 - df["attendance"]
    df["academic_risk"] = ((10 - df["assignments_completed"]) * 10 + (100 - df["exam_score"])) / 2
    df["engagement_risk"] = 100 - df["engagement_score"]
    print("[Feature Engineering] Risk features created.")
    return df
