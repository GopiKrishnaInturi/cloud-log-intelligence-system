from sqlalchemy import Column, Integer, String, DateTime
from storage import Base
import datetime

class InfrastructureLog(Base):
    __tablename__ = "infrastructure_logs"

    id = Column(Integer, primary_key=True, index=True)
    service_name = Column(String)
    severity = Column(String)
    message = Column(String)
    source_host = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)