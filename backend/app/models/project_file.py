import uuid

from sqlalchemy import (
    Column,
    String,
    Integer,
    Text,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.base import Base


class ProjectFile(Base):

    __tablename__ = "project_files"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    project_id = Column(
        String,
        ForeignKey("projects.id"),
        nullable=False
    )

    filename = Column(
        String,
        nullable=False
    )

    relative_path = Column(
        String,
        nullable=False
    )

    language = Column(
        String,
        nullable=False
    )

    extension = Column(
        String,
        nullable=False
    )

    original_code = Column(
        Text,
        nullable=False
    )

    size = Column(
        Integer,
        nullable=False
    )

    line_count = Column(
        Integer,
        default=0
    )

    uploaded_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    project = relationship(
        "Project",
        back_populates="files"
    )