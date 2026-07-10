from fastapi import APIRouter
from fastapi import Depends
from fastapi import File
from fastapi import HTTPException
from fastapi import UploadFile

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.repositories.code_metric_repository import (
    CodeMetricRepository,
)

from app.services.upload.upload_service import UploadService


router = APIRouter()


@router.post("/upload")
def upload_project(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):

    try:

        service = UploadService(db)

        project = service.upload_file(file)

        return {

            "success": True,

            "message": "Project uploaded successfully.",

            "project_id": project.id,

            "project_name": project.name,

            "workspace": project.workspace,

            "status": project.status,

        }

    except Exception as ex:

        raise HTTPException(

            status_code=400,

            detail=str(ex),

        )


@router.get("/projects")
def get_projects(
    db: Session = Depends(get_db),
):

    service = UploadService(db)

    return service.get_projects()


@router.get("/projects/{project_id}")
def get_project(
    project_id: str,
    db: Session = Depends(get_db),
):

    service = UploadService(db)

    return service.get_project(project_id)


@router.get("/projects/{project_id}/files")
def get_project_files(
    project_id: str,
    db: Session = Depends(get_db),
):

    service = UploadService(db)

    return service.get_project_files(project_id)


@router.delete("/projects/{project_id}")
def delete_project(
    project_id: str,
    db: Session = Depends(get_db),
):

    service = UploadService(db)

    service.delete_project(project_id)

    return {

        "message": "Project deleted successfully."

    }


@router.get("/metrics")
def get_metrics(
    db: Session = Depends(get_db),
):

    repository = CodeMetricRepository(db)

    return repository.get_all()

from fastapi import APIRouter
from fastapi import Depends
from fastapi import UploadFile
from fastapi import File
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.upload.upload_service import UploadService

router = APIRouter()


@router.post("/upload/file")
def upload_file(

    file: UploadFile = File(...),

    db: Session = Depends(get_db)

):

    try:

        service = UploadService(db)

        return service.upload_file(file)

    except Exception as ex:

        raise HTTPException(

            status_code=400,

            detail=str(ex)

        )