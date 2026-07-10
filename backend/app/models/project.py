import uuid

from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.base import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    name = Column(
        String,
        nullable=False
    )

    language = Column(
        String,
        default="Python"
    )

    upload_type = Column(
        String,
        default="LOCAL"
    )

    github_url = Column(
        String,
        nullable=True
    )

    workspace = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        default="UPLOADED"
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    files = relationship(
    "ProjectFile",
    back_populates="project",
    cascade="all, delete-orphan"
)