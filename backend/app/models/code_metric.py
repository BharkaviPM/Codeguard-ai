import uuid

from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import relationship

from app.database.base import Base


class CodeMetric(Base):

    __tablename__ = "code_metrics"

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

    total_lines = Column(Integer, default=0)

    blank_lines = Column(Integer, default=0)

    comment_lines = Column(Integer, default=0)

    code_lines = Column(Integer, default=0)

    function_count = Column(Integer, default=0)

    class_count = Column(Integer, default=0)

    import_count = Column(Integer, default=0)

    average_function_length = Column(Integer, default=0)

    long_functions = Column(Integer, default=0)