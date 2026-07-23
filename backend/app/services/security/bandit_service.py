from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

from app.agents.analysis.models import AnalysisResult
from app.analyzers.base import BaseAnalyzer
from app.services.analysis.result_parser import ResultParser


class BanditAnalyzer(BaseAnalyzer):
    """
    Security analyzer using Bandit.

    Detects:
    - Hardcoded passwords
    - Command injection
    - SQL injection
    - Unsafe YAML loading
    - Weak cryptography
    - Shell=True usage
    - Pickle deserialization
    """

    name = "Bandit"

    supported_languages = ["Python"]

    def analyze(
        self,
        project_path: str,
    ) -> AnalysisResult:

        start_time = time.perf_counter()

        result = AnalysisResult(
            analyzer=self.name,
            findings=[],
            metrics={},
            execution_time=0.0,
        )

        project = Path(project_path)

        if not project.exists():
            result.metrics["error"] = "Project path not found"
            return result

        try:

            process = subprocess.run(
                [
                    "bandit",
                    "-r",
                    str(project),
                    "-f",
                    "json",
                ],
                capture_output=True,
                text=True,
                check=False,
            )

            stdout = process.stdout.strip()

            if not stdout:

                result.metrics = {
                    "files_scanned": 0,
                    "issues": 0,
                    "status": "clean",
                }

                result.execution_time = round(
                    time.perf_counter() - start_time,
                    3,
                )

                return result

            report = json.loads(stdout)

        except FileNotFoundError:

            result.metrics["error"] = (
                "Bandit is not installed."
            )

            result.execution_time = round(
                time.perf_counter() - start_time,
                3,
            )

            return result

        except json.JSONDecodeError:

            result.metrics["error"] = (
                "Unable to parse Bandit JSON output."
            )

            result.execution_time = round(
                time.perf_counter() - start_time,
                3,
            )

            return result

        except Exception as ex:

            result.metrics["error"] = str(ex)

            result.execution_time = round(
                time.perf_counter() - start_time,
                3,
            )

            return result

        findings = ResultParser.parse_bandit(
            report.get("results", [])
        )

        result.findings.extend(findings)

        severity_counter = {
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "info": 0,
        }

        confidence_counter = {
            "high": 0,
            "medium": 0,
            "low": 0,
        }

        for issue in report.get("results", []):

            severity = (
                issue.get("issue_severity", "")
                .lower()
            )

            if severity in severity_counter:
                severity_counter[severity] += 1

            confidence = (
                issue.get("issue_confidence", "")
                .lower()
            )

            if confidence in confidence_counter:
                confidence_counter[confidence] += 1

        metrics = report.get("metrics", {})

        files_scanned = len(metrics)

        loc = 0

        for file_metrics in metrics.values():

            loc += file_metrics.get("loc", 0)

        result.metrics = {
            "files_scanned": files_scanned,
            "lines_of_code": loc,
            "issues": len(findings),
            "severity": severity_counter,
            "confidence": confidence_counter,
        }

        result.execution_time = round(
            time.perf_counter() - start_time,
            3,
        )

        return result