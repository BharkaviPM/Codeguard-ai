from typing import Optional
from pydantic import BaseModel


# ==========================
# Code Submission
# ==========================

class CodeSubmission(BaseModel):
    code: str
    language: Optional[str] = None


# ==========================
# Upload Response
# ==========================

class UploadResponse(BaseModel):
    project_id: str
    filename: str
    language: str
    status: str


# ==========================
# Finding Schema
# ==========================

class FindingSchema(BaseModel):
    agent: str
    severity: str
    title: str
    description: str
    line_number: int
    suggestion: str


# ==========================
# Chat Schema
# ==========================

class ChatRequest(BaseModel):
    project_id: str
    question: str


class ChatResponse(BaseModel):
    answer: str