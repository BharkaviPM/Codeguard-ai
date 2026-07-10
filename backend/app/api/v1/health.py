from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    return {
        "status": "OK",
        "message": "CodeGuard AI Backend is running"
    }