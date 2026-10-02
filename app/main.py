from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.schema import PredictionRequest, PredictionResponse
from app.predict import predict_dropout
from pipelines.evaluation import load_metrics


BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"


app = FastAPI(
    title="MLOpsFlow Student Dropout Risk API",
    description="FastAPI service for real-time inference from an end-to-end MLOps pipeline.",
    version="1.0.0",
)


app.mount(
    "/frontend",
    StaticFiles(directory=FRONTEND_DIR),
    name="frontend",
)


@app.get("/")
def root():
    return FileResponse(FRONTEND_DIR / "index.html")


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/metrics")
def metrics():
    try:
        return load_metrics()
    except Exception as exc:
        raise HTTPException(status_code=404, detail=str(exc))


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    try:
        return predict_dropout(request.model_dump())
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))