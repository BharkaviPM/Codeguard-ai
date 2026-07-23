from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.services.analysis.analysis_service import AnalysisService

router = APIRouter()


@router.post("/analyze/{project_id}")
def analyze_project(
    project_id: str,
    db: Session = Depends(get_db),
):

    try:

        service = AnalysisService(db)

        return service.analyze(project_id)

    except Exception as ex:

        raise HTTPException(
            status_code=400,
            detail=str(ex),
        )


@router.get("/results/{project_id}")
def get_results(
    project_id: str,
    db: Session = Depends(get_db),
):

    service = AnalysisService(db)

    return service.get_results(project_id)


@router.get("/summary/{project_id}")
def get_summary(
    project_id: str,
    db: Session = Depends(get_db),
):

    service = AnalysisService(db)

    return service.get_summary(project_id)