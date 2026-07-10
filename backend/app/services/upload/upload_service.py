from pathlib import Path

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.models.project import Project
from app.models.project_file import ProjectFile

from app.repositories.project_repository import ProjectRepository
from app.repositories.project_file_repository import ProjectFileRepository

from app.services.workspace.manager import WorkspaceManager
from app.services.upload.validation_service import ValidationService
from app.services.upload.syntax_validator import SyntaxValidator
from app.services.scanner.scanner_service import ScannerService


class UploadService:

    def __init__(self, db: Session):

        self.db = db

        self.workspace = WorkspaceManager()

        self.project_repository = ProjectRepository(db)

        self.project_file_repository = ProjectFileRepository(db)

        self.validation = ValidationService(db)

        self.syntax = SyntaxValidator()

        self.scanner = ScannerService(db)

    def upload_file(self, file: UploadFile):

        if not file.filename:
            raise ValueError("No file selected.")

        # Read uploaded file
        file_bytes = file.file.read()

        extension = Path(file.filename).suffix.lower()

        # Validate file
        self.validation.validate_extension(extension)
        self.validation.validate_empty(file_bytes)
        self.validation.validate_size(file_bytes)
        self.validation.validate_utf8(file_bytes)

        language = self.validation.detect_language(extension)

        source_code = file_bytes.decode("utf-8")

        syntax_result = self.syntax.validate(
            language,
            source_code
        )

        if not syntax_result["valid"]:
            raise ValueError(
                syntax_result["error"]
            )

        # Create workspace
        workspace = self.workspace.create_workspace()

        source_folder = Path(workspace["workspace"]) / "source"
        source_folder.mkdir(parents=True, exist_ok=True)

        destination = source_folder / file.filename
        destination.write_bytes(file_bytes)

        # Save project
        project = Project(

            id=workspace["project_id"],

            name=file.filename,

            language=language,

            upload_type="LOCAL",

            github_url=None,

            workspace=workspace["workspace"],

            status="UPLOADED"

        )

        project = self.project_repository.create(project)

        # Save uploaded file information
        project_file = ProjectFile(

            project_id=project.id,

            filename=file.filename,

            relative_path=file.filename,

            language=language,

            extension=extension,

            original_code=source_code,

            size=len(file_bytes),

            line_count=len(source_code.splitlines())

        )

        self.project_file_repository.create(project_file)

        # Scan project
        self.scanner.scan_project(

            project.id,

            project.workspace

        )

        return {

            "success": True,

            "project_id": project.id,

            "project_name": project.name,

            "language": language,

            "workspace": project.workspace,

            "filename": file.filename,

            "status": project.status,

            "syntax_valid": True

        }

    def get_project(self, project_id: str):

        project = self.project_repository.get(project_id)

        if not project:
            raise ValueError("Project not found.")

        return project

    def get_projects(self):

        return self.project_repository.get_all()

    def delete_project(self, project_id: str):

        project = self.project_repository.delete(project_id)

        if not project:
            raise ValueError("Project not found.")

        return project

    def get_project_files(self, project_id: str):

        return self.project_file_repository.get_by_project(project_id)