import json
from pipelines.config import REPORT_PATH

def load_metrics():
    if not REPORT_PATH.exists():
        raise FileNotFoundError("Metrics report not found. Run training first.")
    return json.loads(REPORT_PATH.read_text(encoding="utf-8"))

if __name__ == "__main__":
    print(load_metrics())
