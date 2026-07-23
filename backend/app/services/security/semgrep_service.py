from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path
from typing import Any

from app.agents.analysis.models import AnalysisResult
from app.analyzers.base import BaseAnalyzer
from app.services.analysis.result_parser import ResultParser


class SemgrepAnalyzer(BaseAnalyzer):
    """
    Semgrep Security Analyzer

    Performs static security analysis using Semgrep.

    Detects:
        • SQL Injection
        • Command Injection
        • Hardcoded Secrets
        • Path Traversal
        • SSRF
        • XSS
        • Insecure Deserialization
        • Weak Cryptography
        • Authentication Issues
        • OWASP Top 10 Vulnerabilities

    Returns:
        AnalysisResult
    """

    name = "Semgrep"

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

            result.execution_time = round(
                time.perf_counter() - start_time,
                3,
            )

            return result

        try:

            process = subprocess.run(
                [
                    "semgrep",
                    "--config",
                    "auto",
                    "--json",
                    str(project),
                ],
                capture_output=True,
                text=True,
                check=False,
            )

        except FileNotFoundError:

            result.metrics["error"] = (
                "Semgrep is not installed."
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

        stdout = process.stdout.strip()

        if not stdout:

            result.metrics = {
                "files_scanned": 0,
                "rules_executed": 0,
                "issues": 0,
                "status": "clean",
            }

            result.execution_time = round(
                time.perf_counter() - start_time,
                3,
            )

            return result

        try:

            report = json.loads(stdout)

        except json.JSONDecodeError:

            result.metrics["error"] = (
                "Invalid Semgrep JSON output."
            )

            result.execution_time = round(
                time.perf_counter() - start_time,
                3,
            )

            return result

        results = report.get("results", [])

        severity_counter = {
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "info": 0,
        }

        rule_counter: dict[str, int] = {}

        language_counter: dict[str, int] = {}

        file_counter: set[str] = set()

        # -------- Part 2 continues from here --------
        # The next section will:
        # • Convert Semgrep results into Finding objects
        # • Aggregate severity statistics
        # • Count rules executed
        # • Count scanned files
        # • Populate AnalysisResult.metrics
        # • Set execution_time
        # • Return AnalysisResult

        findings = ResultParser.parse_semgrep(results)

        result.findings.extend(findings)

        for issue in results:

            extra: dict[str, Any] = issue.get(
                "extra",
                {},
            )

            severity = (
                extra.get(
                    "severity",
                    "INFO",
                )
                .lower()
            )

            if severity in severity_counter:

                severity_counter[
                    severity
                ] += 1

            else:

                severity_counter[
                    "info"
                ] += 1

            rule_id = issue.get(
                "check_id",
                "unknown",
            )

            rule_counter[rule_id] = (
                rule_counter.get(
                    rule_id,
                    0,
                )
                + 1
            )

            file_counter.add(
                issue.get(
                    "path",
                    "",
                )
            )

            language = (
                issue.get(
                    "language",
                    "unknown",
                )
                .lower()
            )

            language_counter[
                language
            ] = (
                language_counter.get(
                    language,
                    0,
                )
                + 1
            )

        statistics = report.get(
            "statistics",
            {},
        )

        engine_requested = (
            statistics.get(
                "rules",
                {}
            )
            if isinstance(
                statistics,
                dict,
            )
            else {}
        )

        rules_executed = 0

        if isinstance(
            engine_requested,
            dict,
        ):

            rules_executed = (
                engine_requested.get(
                    "executed",
                    len(rule_counter),
                )
            )

        elif isinstance(
            engine_requested,
            list,
        ):

            rules_executed = len(
                engine_requested
            )

        else:

            rules_executed = len(
                rule_counter
            )

        result.metrics = {
            "files_scanned": len(
                file_counter
            ),
            "rules_executed": rules_executed,
            "issues": len(
                findings
            ),
            "severity": severity_counter,
            "languages": language_counter,
            "top_rules": dict(
                sorted(
                    rule_counter.items(),
                    key=lambda item: item[
                        1
                    ],
                    reverse=True,
                )[:10]
            ),
        }

        result.execution_time = round(
            time.perf_counter()
            - start_time,
            3,
        )

        return result