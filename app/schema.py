from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    attendance: float = Field(..., ge=0, le=100)
    assignments_completed: int = Field(..., ge=0, le=10)
    exam_score: float = Field(..., ge=0, le=100)
    engagement_score: float = Field(..., ge=0, le=100)

class PredictionResponse(BaseModel):
    dropout_risk: str
    confidence: float
    risk_probability: float
