from fastapi import FastAPI
from app.api import resume, auth

app = FastAPI(
    title="AI Career Intelligence Platform",
    version="1.0.0"
)

app.include_router(
    resume.router,
    prefix="/resume",
    tags=["Resume"]
)

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)


@app.get("/")
def home():
    return {
        "message": "AI Career Intelligence Platform API"
    }

@app.get("/health")
def health():
    return {
        "status": "running"
    }
