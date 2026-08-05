from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.schemas import CodeSubmission

from app.services.upload_service import UploadService

router = APIRouter()


@router.post("/upload")
def upload_code(
    request: CodeSubmission,
    db: Session = Depends(get_db)
):

    filename = (
        "code.py"
        if request.language == "Python"
        else "code.java"
    )

    return UploadService.save_code(
        db=db,
        filename=filename,
        code=request.code,
    )