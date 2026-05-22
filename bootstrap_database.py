from storage import Base, engine
from entities import InfrastructureLog

Base.metadata.create_all(bind=engine)

print("Infrastructure database initialized")