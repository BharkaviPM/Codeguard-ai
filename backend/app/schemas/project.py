from datetime import datetime

from pydantic import BaseModel


class ProjectResponse(BaseModel):

    id: str
    name: str
    language: str
    upload_type: str
    workspace: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class UploadResponse(BaseModel):

    success: bool
    message: str
    project: ProjectResponse