from fastapi import FastAPI
from app.api import resume, auth
from app.database.db import Base, engine

# Import all models so SQLAlchemy knows about them before creating tables
from app.models import user  # noqa: F401

# Auto-create all tables that don't exist yet (safe to run on every startup)
Base.metadata.create_all(bind=engine)

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
