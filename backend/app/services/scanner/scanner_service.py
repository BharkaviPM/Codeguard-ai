from pathlib import Path

from sqlalchemy.orm import Session

from app.models.code_metric import CodeMetric

from app.repositories.project_file_repository import (
    ProjectFileRepository,
)
from app.repositories.code_metric_repository import (
    CodeMetricRepository,
)

from app.services.scanner.analyzer import ASTAnalyzer
from app.services.scanner.metrics_service import MetricsService
from app.services.scanner.radon_service import RadonService


class ScannerService:

    def __init__(self, db: Session):

        self.db = db

        self.project_file_repository = ProjectFileRepository(db)
        self.metric_repository = CodeMetricRepository(db)

        self.analyzer = ASTAnalyzer()
        self.metrics = MetricsService()
        self.radon = RadonService()

    def scan_project(
        self,
        project_id: str,
        workspace: str,
    ):

        source_folder = Path(workspace) / "source"

        project_files = self.project_file_repository.get_by_project(
            project_id
        )

        scanned_files = []

        for project_file in project_files:

            file_path = (
                source_folder /
                project_file.relative_path
            )

            if not file_path.exists():
                continue

            # AST Analysis
            self.analyzer.analyze(file_path)

            # Code Metrics
            metrics = self.metrics.calculate(file_path)

            # Radon Analysis
            self.radon.analyze(file_path)

            metric = CodeMetric(

                project_file_id=project_file.id,

                total_lines=metrics["total_lines"],

                blank_lines=metrics["blank_lines"],

                comment_lines=metrics["comment_lines"],

                code_lines=metrics["code_lines"],

                function_count=metrics["function_count"],

                class_count=metrics["class_count"],

                import_count=metrics["import_count"],

                average_function_length=metrics[
                    "average_function_length"
                ],

                long_functions=metrics[
                    "long_functions"
                ],

            )

            self.metric_repository.create(metric)

            scanned_files.append(project_file)

        return scanned_files