from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = BASE_DIR / "data" / "raw" / "students.csv"
PROCESSED_DATA_PATH = BASE_DIR / "data" / "processed" / "processed_data.csv"
MODEL_PATH = BASE_DIR / "models" / "trained_model.pkl"
REPORT_PATH = BASE_DIR / "reports" / "metrics.json"

TARGET_COLUMN = "dropout"
FEATURE_COLUMNS = [
    "attendance",
    "assignments_completed",
    "exam_score",
    "engagement_score",
    "attendance_risk",
    "academic_risk",
    "engagement_risk",
]
