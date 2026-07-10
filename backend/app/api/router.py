from fastapi import APIRouter

from app.api.v1.health import router as health_router
from app.api.v1.upload import router as upload_router
from app.api.v1.chat import router as chat_router

api_router = APIRouter()

api_router.include_router(
    health_router,
    tags=["Health"]
)

api_router.include_router(
    upload_router,
    tags=["Upload"]
)

api_router.include_router(
    chat_router,
    tags=["Chat"]
)