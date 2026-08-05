import uuid
from pathlib import Path

from sqlalchemy.orm import Session

from app.database.models import Project
from app.core.config import UPLOAD_FOLDER
from app.services.syntax_checker import SyntaxChecker


class UploadService:

    @staticmethod
    def save_code(
        db: Session,
        filename: str,
        code: str,
    ):

        # Detect Language
        language = SyntaxChecker.detect_language(
            filename=filename,
            code=code
        )

        # Validate Syntax
        valid, message = SyntaxChecker.validate(
            language,
            code
        )

        if not valid:
            raise Exception(message)

        # Create Upload Folder
        UPLOAD_FOLDER.mkdir(
            parents=True,
            exist_ok=True
        )

        # Generate Unique Filename
        extension = Path(filename).suffix

        unique_name = f"{uuid.uuid4()}{extension}"

        file_path = UPLOAD_FOLDER / unique_name

        # Save File
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(code)

        # Save to Database
        project = Project(
            filename=unique_name,
            language=language,
        )

        db.add(project)
        db.commit()
        db.refresh(project)

        return {
            "project_id": str(project.id),
            "filename": unique_name,
            "language": language,
            "status": "Uploaded Successfully"
        }