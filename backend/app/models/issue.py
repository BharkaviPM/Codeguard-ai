import uuid

from sqlalchemy import Column, ForeignKey, Integer, String, Text

from app.database.base import Base


class Issue(Base):

    __tablename__ = "issues"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    project_file_id = Column(
        String,
        ForeignKey("project_files.id"),
        nullable=False
    )

    tool = Column(
        String,
        nullable=False
    )

    severity = Column(
        String,
        nullable=False
    )

    line = Column(
        Integer,
        nullable=False
    )

    code = Column(
        String,
        nullable=False
    )

    message = Column(
        Text,
        nullable=False
    )