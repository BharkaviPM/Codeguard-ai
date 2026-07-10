from pathlib import Path

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.models.project_file import ProjectFile


class ValidationService:

    ALLOWED_EXTENSIONS = {
        ".py",
        ".java"
    }

    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB

    def __init__(self, db: Session):
        self.db = db

    def validate_upload(
        self,
        project_id: str,
        file: UploadFile,
        file_bytes: bytes
    ):

        if not file.filename:
            raise ValueError("No file selected.")

        extension = Path(file.filename).suffix.lower()

        self.validate_extension(extension)

        self.validate_empty(file_bytes)

        self.validate_size(file_bytes)

        self.validate_utf8(file_bytes)

        self.validate_duplicate(
            project_id,
            file.filename
        )

        return self.detect_language(extension)

    def validate_extension(
        self,
        extension: str
    ):

        if extension not in self.ALLOWED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )

    def validate_size(
        self,
        file_bytes: bytes
    ):

        if len(file_bytes) > self.MAX_FILE_SIZE:
            raise ValueError(
                "Maximum file size is 5 MB."
            )

    def validate_empty(
        self,
        file_bytes: bytes
    ):

        if len(file_bytes) == 0:
            raise ValueError(
                "Uploaded file is empty."
            )

    def validate_utf8(
        self,
        file_bytes: bytes
    ):

        try:
            file_bytes.decode("utf-8")

        except UnicodeDecodeError:

            raise ValueError(
                "File must be UTF-8 encoded."
            )

    def validate_duplicate(
        self,
        project_id: str,
        filename: str
    ):

        existing = (

            self.db.query(ProjectFile)

            .filter(
                ProjectFile.project_id == project_id
            )

            .filter(
                ProjectFile.filename == filename
            )

            .first()

        )

        if existing:

            raise ValueError(
                "A file with the same name already exists."
            )

    def detect_language(
        self,
        extension: str
    ):

        mapping = {

            ".py": "Python",

            ".java": "Java"

        }

        return mapping.get(
            extension,
            "Unknown"
        )