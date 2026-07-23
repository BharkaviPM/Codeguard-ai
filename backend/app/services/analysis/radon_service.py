import time
from pathlib import Path

from radon.complexity import cc_visit
from radon.metrics import h_visit

from app.agents.analysis.models import AnalysisResult
from app.analyzers.base import BaseAnalyzer
from app.services.analysis.result_parser import ResultParser


class RadonAnalyzer(BaseAnalyzer):
    """
    Radon Analyzer

    Performs:
        • Cyclomatic Complexity
        • Halstead Metrics
        • Maintainability Metrics
    """

    name = "Radon"

    supported_languages = ["Python"]

    def analyze(self, project_path: str) -> AnalysisResult:

        start_time = time.time()

        result = AnalysisResult(
            analyzer=self.name,
            findings=[],
            metrics={},
            execution_time=0.0,
        )

        project = Path(project_path)

        python_files = list(project.rglob("*.py"))

        for file in python_files:

            try:

                source = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

            except Exception:
                continue

            file_metrics = {}

            # -----------------------------------------
            # Cyclomatic Complexity
            # -----------------------------------------

            try:

                complexities = cc_visit(source)

                complexity_list = []

                for block in complexities:

                    complexity_list.append(
                        {
                            "name": block.name,
                            "complexity": block.complexity,
                            "line": block.lineno,
                        }
                    )

                    if block.complexity >= 10:

                        finding = ResultParser.parse_radon(
                            file=str(file),
                            line=block.lineno,
                            complexity=block.complexity,
                            message=(
                                f"{block.name} has high cyclomatic "
                                f"complexity ({block.complexity})"
                            ),
                        )

                        result.findings.append(finding)

                file_metrics["cyclomatic_complexity"] = complexity_list

            except Exception:
                file_metrics["cyclomatic_complexity"] = []

            # -----------------------------------------
            # Halstead Metrics
            # -----------------------------------------

            try:

                halstead = h_visit(source)

                file_metrics["halstead"] = {
                    "h1": halstead.total.h1,
                    "h2": halstead.total.h2,
                    "N1": halstead.total.N1,
                    "N2": halstead.total.N2,
                    "vocabulary": halstead.total.vocabulary,
                    "length": halstead.total.length,
                    "volume": halstead.total.volume,
                    "difficulty": halstead.total.difficulty,
                    "effort": halstead.total.effort,
                }

            except Exception:

                file_metrics["halstead"] = {}

            result.metrics[str(file)] = file_metrics

        result.execution_time = round(
            time.time() - start_time,
            3,
        )

        return result