from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

from app.agents.analysis.models import AnalysisResult
from app.analyzers.base import BaseAnalyzer
from app.services.analysis.result_parser import ResultParser


class PipAuditAnalyzer(BaseAnalyzer):
    """
    pip-audit Security Analyzer

    Detects:

    • Vulnerable packages
    • Known CVEs
    • PYSEC advisories
    • Dependency vulnerabilities
    • Recommended fixed versions
    """

    name = "PipAudit"

    supported_languages = ["Python"]

    REQUIREMENT_FILES = (
        "requirements.txt",
        "requirements-dev.txt",
        "requirements-prod.txt",
        "requirements/base.txt",
        "requirements/common.txt",
        "pyproject.toml",
        "Pipfile",
        "poetry.lock",
    )

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

        dependency_file = self._find_dependency_file(project)

        if dependency_file is None:

            result.metrics = {
                "status": "No dependency file found",
                "issues": 0,
            }

            result.execution_time = round(
                time.perf_counter() - start,
                3,
            )

            return result

        try:

            process = subprocess.run(
                [
                    "pip-audit",
                    "--format",
                    "json",
                    "--requirement",
                    str(dependency_file),
                ],
                capture_output=True,
                text=True,
                check=False,
            )

        except FileNotFoundError:

            result.metrics["error"] = (
                "pip-audit is not installed."
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

        stdout = process.stdout.strip()

        if not stdout:

            result.metrics = {
                "dependency_file": str(dependency_file),
                "packages": 0,
                "issues": 0,
                "status": "clean",
            }

            result.execution_time = round(
                time.perf_counter() - start,
                3,
            )

            return result

        try:

            report = json.loads(stdout)

        except json.JSONDecodeError:

            result.metrics["error"] = (
                "Unable to parse pip-audit JSON."
            )

            result.execution_time = round(
                time.perf_counter() - start,
                3,
            )

            return result

        findings = []

        vulnerable_packages = 0
        vulnerability_count = 0

        severity_counter = {
            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0,
            "info": 0,
        }

        dependencies = report.get(
            "dependencies",
            [],
        )

        for package in dependencies:

            vulns = package.get(
                "vulns",
                [],
            )

            if not vulns:
                continue

            vulnerable_packages += 1

            package_name = package.get(
                "name",
                "unknown",
            )

            package_version = package.get(
                "version",
                "",
            )

            for vuln in vulns:

                vulnerability_count += 1

                fix_versions = vuln.get(
                    "fix_versions",
                    [],
                )

                severity = "HIGH"

                severity_counter[
                    severity.lower()
                ] += 1

                findings.append(

                    ResultParser.create_finding(
                        tool="PipAudit",
                        file=str(dependency_file),
                        line=0,
                        column=0,
                        severity=severity,
                        rule=vuln.get(
                            "id",
                            "UNKNOWN",
                        ),
                        message=(
                            f"{package_name}"
                            f" ({package_version}) "
                            f"is affected by "
                            f"{vuln.get('id')}."
                            f" Upgrade to "
                            f"{', '.join(fix_versions) if fix_versions else 'latest version'}."
                        ),
                    )

                )

        result.findings.extend(findings)

        result.metrics = {
            "dependency_file": str(
                dependency_file,
            ),
            "packages_scanned": len(
                dependencies,
            ),
            "vulnerable_packages": vulnerable_packages,
            "vulnerabilities": vulnerability_count,
            "severity": severity_counter,
        }

        result.execution_time = round(
            time.perf_counter() - start,
            3,
        )

        return result

    def _find_dependency_file(
        self,
        project: Path,
    ) -> Path | None:
        """
        Locate the dependency manifest.
        """

        for name in self.REQUIREMENT_FILES:

            candidate = project / name

            if candidate.exists():

                return candidate

        return None