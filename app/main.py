from fastapi import FastAPI

from app.database.database import Base, engine
from app.database import models

from app.api.upload import router as upload_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CodeGuard v3",
    version="1.0.0",
)

app.include_router(upload_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to CodeGuard v3"
    }