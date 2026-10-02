from fastapi import FastAPI, HTTPException
from app.schema import PredictionRequest, PredictionResponse
from app.predict import predict_dropout
from pipelines.evaluation import load_metrics

app = FastAPI(
    title="MLOpsFlow Student Dropout Risk API",
    description="FastAPI service for real-time inference from an end-to-end MLOps pipeline.",
    version="1.0.0",
)

@app.get("/")
def root():
    return {
        "message": "MLOpsFlow API is running",
        "docs": "/docs",
        "health": "/health",
    }

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
