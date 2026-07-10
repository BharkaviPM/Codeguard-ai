from sqlalchemy.orm import Session

from app.models.code_metric import CodeMetric


class CodeMetricRepository:

    def __init__(self, db: Session):

        self.db = db

    def create(self, metric: CodeMetric):

        self.db.add(metric)

        self.db.commit()

        self.db.refresh(metric)

        return metric

    def get_by_project_file(
        self,
        project_file_id: str
    ):

        return (

            self.db.query(CodeMetric)

            .filter(
                CodeMetric.project_file_id == project_file_id
            )

            .first()

        )

    def get_all(self):

        return self.db.query(CodeMetric).all()