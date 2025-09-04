from pydantic import BaseModel, Field

class PredictRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Tweet or sentence to classify")

class PredictResponse(BaseModel):
    label: str
    probability: float
    label_id: int
    model_version: str = "logreg-v1"

class HealthResponse(BaseModel):
    status: str
