from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

from app.agents.analysis.models import AnalysisResult
from app.analyzers.base import BaseAnalyzer
from app.services.analysis.result_parser import ResultParser


class DetectSecretsAnalyzer(BaseAnalyzer):
    """
    Detect-Secrets Analyzer

    Detects:
        • AWS Keys
        • Azure Keys
        • GCP Keys
        • GitHub Tokens
        • Slack Tokens
        • JWT Tokens
        • Private Keys
        • Passwords
        • API Keys
        • High Entropy Strings
    """

    name = "DetectSecrets"

    supported_languages = [
        "Python",
        "Java",
        "JavaScript",
        "TypeScript",
        "Go",
        "C",
        "C++",
    ]

    def analyze(
        self,
        project_path: str,
    ) -> AnalysisResult:

        start = time.perf_counter()

        result = AnalysisResult(
            analyzer=self.name,
            findings=[],
            metrics={},
            execution_time=0.0,
        )

        project = Path(project_path)

        if not project.exists():

            result.metrics["error"] = "Project path not found"

            result.execution_time = round(
                time.perf_counter() - start,
                3,
            )

            return result

        try:

            process = subprocess.run(
                [
                    "detect-secrets",
                    "scan",
                    str(project),
                ],
                capture_output=True,
                text=True,
                check=False,
            )

        except FileNotFoundError:

            result.metrics["error"] = (
                "detect-secrets is not installed."
            )

            result.execution_time = round(
                time.perf_counter() - start,
                3,
            )

            return result

        except Exception as ex:

            result.metrics["error"] = str(ex)

            result.execution_time = round(
                time.perf_counter() - start,
                3,
            )

            return result

        if not process.stdout.strip():

            result.metrics = {
                "files_scanned": 0,
                "issues": 0,
                "status": "clean",
            }

            result.execution_time = round(
                time.perf_counter() - start,
                3,
            )

            return result

        try:

            report = json.loads(process.stdout)

        except json.JSONDecodeError:

            result.metrics["error"] = (
                "Invalid detect-secrets output."
            )

            result.execution_time = round(
                time.perf_counter() - start,
                3,
            )

            return result

        findings = []

        plugin_counter = {}

        file_counter = set()

        results = report.get("results", {})

        for filename, secrets in results.items():

            file_counter.add(filename)

            for secret in secrets:

                findings.append(
                    ResultParser.create_finding(
                        tool="DetectSecrets",
                        file=filename,
                        line=secret.get("line_number", 0),
                        column=0,
                        message=(
                            f"Potential secret detected "
                            f"({secret.get('type', 'Unknown')})"
                        ),
                        severity="HIGH",
                        rule=secret.get(
                            "type",
                            "Secret",
                        ),
                    )
                )

                plugin = secret.get(
                    "type",
                    "Unknown",
                )

                plugin_counter[plugin] = (
                    plugin_counter.get(
                        plugin,
                        0,
                    )
                    + 1
                )

        result.findings.extend(findings)

        result.metrics = {
            "files_scanned": len(file_counter),
            "issues": len(findings),
            "secret_types": plugin_counter,
            "plugins_enabled": len(
                report.get(
                    "plugins_used",
                    []
                )
            ),
            "filters_enabled": len(
                report.get(
                    "filters_used",
                    []
                )
            ),
        }

        result.execution_time = round(
            time.perf_counter() - start,
            3,
        )

        return result