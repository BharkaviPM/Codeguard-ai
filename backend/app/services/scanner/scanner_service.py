from pathlib import Path

from sqlalchemy.orm import Session

from app.models.project_file import ProjectFile
from app.models.code_metric import CodeMetric

from app.repositories.project_file_repository import ProjectFileRepository
from app.repositories.code_metric_repository import CodeMetricRepository

from app.services.scanner.analyzer import ASTAnalyzer
from app.services.scanner.metrics_service import MetricsService
from app.services.scanner.radon_service import RadonService
from app.services.analysis.flake8_service import Flake8Service
from app.models.issue import Issue

from app.repositories.issue_repository import IssueRepository
from app.models.project_file import ProjectFile


class ScannerService:

    def __init__(self, db: Session):

        self.db = db

        self.project_file_repository = ProjectFileRepository(db)

        self.metric_repository = CodeMetricRepository(db)

        self.analyzer = ASTAnalyzer()

        self.metrics = MetricsService()

        self.radon = RadonService()

        self.flake8 = Flake8Service()

        self.issue_repository = IssueRepository(db)

    def scan_project(
        self,
        project_id: str,
        workspace: str,
    ):

        source = Path(workspace) / "source"

        scanned_files = []

        for file in source.rglob("*"):

            if not file.is_file():
                continue

            try:

                with open(
                    file,
                    "r",
                    encoding="utf-8",
                    errors="ignore",
                ) as f:

                    line_count = len(f.readlines())

            except Exception:

                line_count = 0

            # ---------- AST ----------
            ast_result = self.analyzer.analyze(file)

            # ---------- Metrics ----------
            metrics = self.metrics.calculate(file)

            # ---------- Radon ----------
            radon = self.radon.analyze(file)

            print("\n========== AST ==========")
            print(ast_result)

            print("\n========== Metrics ==========")
            print(metrics)

            print("\n========== Radon ==========")
            print(radon)

            flake8_issues = self.flake8.analyze(file)

            for issue in flake8_issues:

                db_issue = Issue(

                project_file_id=project_file.id,

                tool="Flake8",

                severity=issue["severity"],

                line=issue["line"],

                code="FLAKE8",

                message=issue["message"]

            )

            self.issue_repository.create(db_issue)

            print("\n========== FLAKE8 ==========")

            print(flake8_issues)

            print("============================\n")

            project_file = ProjectFile(

                project_id=project_id,

                filename=file.name,

                relative_path=str(
                    file.relative_to(source)
                ),

                extension=file.suffix,

                language=self.detect_language(file),

                size=file.stat().st_size,

                line_count=line_count

            )

            project_file = self.project_file_repository.create(
                project_file
            )

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

    def detect_language(self, file: Path):

        mapping = {

            ".py": "Python",

            ".java": "Java",

            ".js": "JavaScript",

            ".ts": "TypeScript",

            ".cpp": "C++",

            ".c": "C",

            ".cs": "C#",

            ".go": "Go",

            ".php": "PHP",

            ".rb": "Ruby",

        }

        return mapping.get(
            file.suffix.lower(),
            "Unknown"
        )
    
    