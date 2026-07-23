import json
import subprocess
import time
from pathlib import Path

from app.analyzers.base import BaseAnalyzer
from app.agents.analysis.models import AnalysisResult
from app.services.analysis.result_parser import ResultParser


class PylintAnalyzer(BaseAnalyzer):
    """
    Pylint Analyzer

    Executes pylint on every Python file in a project and converts
    the JSON output into unified Finding objects.
    """

    name = "Pylint"

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

        total_messages = 0

        for file in python_files:

            try:

                process = subprocess.run(
                    [
                        "pylint",
                        str(file),
                        "--output-format=json",
                        "--score=n",
                    ],
                    capture_output=True,
                    text=True,
                    check=False,
                )

                if not process.stdout.strip():

                    result.metrics[str(file)] = {
                        "messages": 0,
                        "status": "clean",
                    }

                    continue

                pylint_output = json.loads(process.stdout)

                findings = ResultParser.parse_pylint(
                    pylint_output
                )

                result.findings.extend(findings)

                total_messages += len(findings)

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
                    "messages": len(findings),
                    "severity": severity_counter,
                }

            except json.JSONDecodeError:

                result.metrics[str(file)] = {
                    "messages": 0,
                    "status": "json_parse_failed",
                }

            except Exception as ex:

                result.metrics[str(file)] = {
                    "messages": 0,
                    "status": "failed",
                    "error": str(ex),
                }

        result.metrics["summary"] = {
            "files_scanned": len(python_files),
            "total_messages": total_messages,
        }

        result.execution_time = round(
            time.time() - start_time,
            3,
        )

        return result