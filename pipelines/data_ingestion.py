import pandas as pd
from pipelines.config import RAW_DATA_PATH

def load_data(path=RAW_DATA_PATH) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found at {path}")
    df = pd.read_csv(path)
    print(f"[Data Ingestion] Loaded {len(df)} rows from {path}")
    return df

if __name__ == "__main__":
    load_data()
