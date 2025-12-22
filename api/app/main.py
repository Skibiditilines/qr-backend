from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title="Avon QR API", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "Welcome to Avon QR API"}
