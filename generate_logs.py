import random
from storage import SessionLocal
from entities import InfrastructureLog

db = SessionLocal()

levels = ["INFO", "WARN", "ERROR", "CRITICAL"]

for i in range(250):
    log = InfrastructureLog(
        service_name=f"service_{i}",
        severity=random.choice(levels),
        message="Infrastructure monitoring event",
        source_host=f"server-{i}"
    )
    db.add(log)

db.commit()

print("Synthetic logs generated")