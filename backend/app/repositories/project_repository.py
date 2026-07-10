from sqlalchemy.orm import Session

from app.models.project import Project


class ProjectRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, project: Project):

        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)

        return project

    def get(self, project_id: str):

        return (
            self.db.query(Project)
            .filter(Project.id == project_id)
            .first()
        )

    def get_all(self):

        return (
            self.db.query(Project)
            .order_by(Project.created_at.desc())
            .all()
        )

    def delete(self, project_id: str):

        project = self.get(project_id)

        if project:

            self.db.delete(project)

            self.db.commit()

        return project

    def update_status(self, project_id: str, status: str):

        project = self.get(project_id)

        if project:

            project.status = status

            self.db.commit()

            self.db.refresh(project)

        return project