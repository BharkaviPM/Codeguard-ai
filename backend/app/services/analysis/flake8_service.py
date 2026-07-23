import subprocess
import time
from pathlib import Path

from app.analyzers.base import BaseAnalyzer
from app.agents.analysis.models import AnalysisResult
from app.services.analysis.result_parser import ResultParser


class Flake8Analyzer(BaseAnalyzer):
    """
    Flake8 Analyzer

    Runs Flake8 on every Python file in the project and converts
    the output into unified Finding objects.
    """

    name = "Flake8"

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

        total_issues = 0

        for file in python_files:

            try:

                process = subprocess.run(
                    [
                        "flake8",
                        str(file),
                        "--max-line-length=100",
                        "--statistics",
                    ],
                    capture_output=True,
                    text=True,
                    check=False,
                )

                stdout = process.stdout.strip()

                if not stdout:

                    result.metrics[str(file)] = {
                        "issues": 0,
                        "status": "clean",
                    }

                    continue

                findings = ResultParser.parse_flake8(
                    stdout.splitlines()
                )

                result.findings.extend(findings)

                total_issues += len(findings)

                severity_counter = {
                    "critical": 0,
                    "high": 0,
                    "medium": 0,
                    "low": 0,
                    "info": 0,
                }

                for finding in findings:

                    severity = finding.severity.value.lower()

                    if severity in severity_counter:
                        severity_counter[severity] += 1

                result.metrics[str(file)] = {
                    "issues": len(findings),
                    "severity": severity_counter,
                }

            except Exception as ex:

                result.metrics[str(file)] = {
                    "issues": 0,
                    "status": "failed",
                    "error": str(ex),
                }

        result.metrics["summary"] = {
            "files_scanned": len(python_files),
            "total_issues": total_issues,
        }

        result.execution_time = round(
            time.time() - start_time,
            3,
        )

        return result