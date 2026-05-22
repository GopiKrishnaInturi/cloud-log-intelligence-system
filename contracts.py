from pydantic import BaseModel

class LogPayload(BaseModel):
    service_name: str
    severity: str
    message: str
    source_host: str