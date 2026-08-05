import uuid

from sqlalchemy import (
    Column,
    String,
    Text,
    Integer,
    DateTime,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import relationship

from sqlalchemy.sql import func

from app.database.database import Base


# =====================================
# Project Table
# =====================================

class Project(Base):

    __tablename__ = "projects"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    filename = Column(String(255), nullable=False)

    language = Column(String(30), nullable=False)

    uploaded_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    findings = relationship(
        "Finding",
        back_populates="project",
        cascade="all, delete",
    )

    chats = relationship(
        "ChatHistory",
        back_populates="project",
        cascade="all, delete",
    )


# =====================================
# Findings Table
# =====================================

class Finding(Base):

    __tablename__ = "findings"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    project_id = Column(
        UUID(as_uuid=True),
        ForeignKey("projects.id"),
    )

    agent = Column(String(50))

    severity = Column(String(20))

    title = Column(String(300))

    description = Column(Text)

    line_number = Column(Integer)

    suggestion = Column(Text)

    project = relationship(
        "Project",
        back_populates="findings",
    )


# =====================================
# Chat History
# =====================================

class ChatHistory(Base):

    __tablename__ = "chat_history"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    project_id = Column(
        UUID(as_uuid=True),
        ForeignKey("projects.id"),
    )

    question = Column(Text)

    answer = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    project = relationship(
        "Project",
        back_populates="chats",
    )