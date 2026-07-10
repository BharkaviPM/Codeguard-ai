from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Register all models

from app.models.project import Project
from app.models.project_file import ProjectFile