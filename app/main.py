from fastapi import FastAPI
from app.core.config import settings
from app.routes import user_routes
from app.models import Account, Concept

app = FastAPI(title="Avon QR API", version="1.0.0", root_path="/api")

app.include_router(user_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Avon QR API"}
