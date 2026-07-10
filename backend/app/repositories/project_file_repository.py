from typing import List

from sqlalchemy.orm import Session

from app.models.project_file import ProjectFile


class ProjectFileRepository:

    def __init__(self, db: Session):

        self.db = db

    def create(
        self,
        project_file: ProjectFile
    ) -> ProjectFile:

        self.db.add(project_file)

        self.db.commit()

        self.db.refresh(project_file)

        return project_file

    def create_many(
        self,
        files: List[ProjectFile]
    ):

        self.db.add_all(files)

        self.db.commit()

        for file in files:

            self.db.refresh(file)

        return files

    def get_by_project(
        self,
        project_id: str
    ):

        return (

            self.db.query(ProjectFile)

            .filter(
                ProjectFile.project_id == project_id
            )

            .order_by(
                ProjectFile.relative_path
            )

            .all()

        )

    def delete_by_project(
        self,
        project_id: str
    ):

        (

            self.db.query(ProjectFile)

            .filter(
                ProjectFile.project_id == project_id
            )

            .delete()

        )

        self.db.commit()