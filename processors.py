from sqlalchemy.orm import Session
from entities import InfrastructureLog

def save_log(db: Session, payload):
    log = InfrastructureLog(**payload.dict())
    db.add(log)
    db.commit()
    db.refresh(log)
    return log