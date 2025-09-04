from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import PredictRequest, PredictResponse, HealthResponse
from app.utils import preprocess_text
import joblib
import numpy as np
from typing import Optional
import os
from fastapi.staticfiles import StaticFiles
from fastapi import Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Offensive Tweet Classifier",
    description="FastAPI wrapper around your trained Logistic Regression model",
    version="1.0.0",
)

# Optional CORS (adjust for your frontend or set to specific origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict_web", response_class=HTMLResponse)
def predict_web(request: Request, text: str = Form(...)):
    clean = preprocess_text(text)
    X = _vectorizer.transform([clean])
    pred_id = int(_model.predict(X)[0])
    prob = 1.0
    if hasattr(_model, "predict_proba"):
        probs = _model.predict_proba(X)[0]
        pred_id = int(np.argmax(probs))
        prob = float(probs[pred_id])
    label = "Offensive" if pred_id == 1 else "Non-Offensive"
    return templates.TemplateResponse("index.html", {"request": request, "result": {"label": label, "probability": prob}})

MODEL_DIR = os.getenv("MODEL_DIR", "models")
_model = None
_vectorizer = None
_label_encoder = None

def _artifact_path(name: str) -> str:
    return os.path.join(MODEL_DIR, name)

def load_artifacts():
    global _model, _vectorizer, _label_encoder
    model_path = _artifact_path("model.pkl")
    vec_path = _artifact_path("vectorizer.pkl")
    le_path = _artifact_path("label_encoder.pkl")
    try:
        _model = joblib.load(model_path)
        _vectorizer = joblib.load(vec_path)
        _label_encoder = joblib.load(le_path)
    except Exception as e:
        raise RuntimeError(f"Failed to load artifacts: {e}")

@app.on_event("startup")
def startup_event():
    load_artifacts()

@app.get("/health", response_model=HealthResponse)
def health():
    ok = all(obj is not None for obj in [_model, _vectorizer, _label_encoder])
    return HealthResponse(status="ok" if ok else "error")

@app.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    if not req.text or not req.text.strip():
        raise HTTPException(status_code=400, detail="Empty text")

    # Preprocess exactly like training
    clean = preprocess_text(req.text)

    # Vectorize and predict
    X = _vectorizer.transform([clean])
    probs: Optional[np.ndarray] = None

    # If classifier supports predict_proba
    if hasattr(_model, "predict_proba"):
        probs = _model.predict_proba(X)[0]
        pred_id = int(np.argmax(probs))
        prob = float(probs[pred_id])
    else:
        # Fallback to decision function or predict
        pred_id = int(_model.predict(X)[0])
        prob = 1.0

    # Decode label
    if hasattr(_label_encoder, "inverse_transform"):
        label = _label_encoder.inverse_transform([pred_id])[0]
    else:
        label = str(pred_id)

    return PredictResponse(
        label=("Offensive" if str(label) == "1" else "Non-Offensive")
              if set(getattr(_label_encoder, "classes_", [])) == {0, 1}
              else str(label),
        probability=prob,
        label_id=pred_id,
    )
