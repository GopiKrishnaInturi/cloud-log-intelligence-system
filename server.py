from fastapi import FastAPI
from endpoints import router

app = FastAPI(title="Cloud Infrastructure Log Intelligence System")

app.include_router(router)