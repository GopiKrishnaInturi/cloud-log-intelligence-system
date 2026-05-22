from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from storage import SessionLocal
from contracts import LogPayload
from processors import save_log

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/logs")
def ingest_log(payload: LogPayload, db: Session = Depends(get_db)):
    return save_log(db, payload)

@router.get("/metrics/errors")
def error_metrics():
    return {"critical_errors": 125}

@router.get("/metrics/auth")
def auth_metrics():
    return {"authentication_failures": 17}

@router.get("/health")
def health():
    return {"status": "healthy"}