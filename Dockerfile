FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    NLTK_DATA=/usr/local/nltk_data

# System deps (build tools often not needed for wheels; add if you hit build issues)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl ca-certificates && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy dependency spec first (better build cache)
COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Pre-fetch NLTK data at build time to avoid runtime downloads
RUN python - <<'PY'
import nltk
for pkg in ["wordnet", "stopwords", "omw-1.4"]:
    try:
        nltk.data.find(f"corpora/{pkg}")
    except LookupError:
        nltk.download(pkg)
PY

# Copy code and model artifacts
COPY app ./app
COPY models ./models

EXPOSE 8000

# Healthcheck (optional)
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
 CMD curl -fsS http://localhost:8000/health || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
