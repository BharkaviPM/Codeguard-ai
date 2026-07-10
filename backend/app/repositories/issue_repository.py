from sqlalchemy.orm import Session

from app.models.issue import Issue


class IssueRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, issue: Issue):
        self.db.add(issue)
        self.db.commit()
        self.db.refresh(issue)
        self.db.add_all([issue])
        self.db.commit()

        return issue

    def get_by_project_file(self, project_file_id: str):
        return (
            self.db.query(Issue)
            .filter(Issue.project_file_id == project_file_id)
            .all()
        )