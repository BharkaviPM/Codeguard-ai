from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings

from app.database.base import Base
from app.database.session import engine

# Create all database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    version="2.0.0"
)

app.include_router(api_router)


@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "version": "2.0.0",
        "status": "Running"
    }