from __future__ import annotations

from pathlib import Path
from typing import Iterable

from app.agents.analysis.models import Finding, Severity


class ResultParser:
    """
    Converts outputs from static analysis tools into
    unified Finding objects.
    """

    @staticmethod
    def severity_from_text(level: str) -> Severity:
        """
        Convert tool-specific severity strings to Severity enum.
        """

        if not level:
            return Severity.INFO

        level = level.upper()

        mapping = {
            "CRITICAL": Severity.CRITICAL,
            "HIGH": Severity.HIGH,
            "MEDIUM": Severity.MEDIUM,
            "LOW": Severity.LOW,
            "INFO": Severity.INFO,
            "WARNING": Severity.MEDIUM,
            "WARN": Severity.MEDIUM,
            "ERROR": Severity.HIGH,
            "CONVENTION": Severity.LOW,
            "REFACTOR": Severity.LOW,
            "STYLE": Severity.LOW,
        }

        return mapping.get(level, Severity.INFO)

    @staticmethod
    def create_finding(
        *,
        tool: str,
        file: str,
        line: int,
        column: int = 0,
        message: str,
        severity: str | Severity = Severity.INFO,
        rule: str | None = None,
    ) -> Finding:
        """
        Create a Finding instance.
        """

        if isinstance(severity, str):
            severity = ResultParser.severity_from_text(severity)

        return Finding(
            tool=tool,
            file=str(file),
            line=line,
            column=column,
            message=message,
            severity=severity,
            rule=rule,
        )

    @staticmethod
    def parse_flake8(lines: Iterable[str]) -> list[Finding]:
        """
        Parse Flake8 stdout.
        Format:
        file.py:12:4:E302 expected 2 blank lines
        """

        findings = []

        for line in lines:

            try:
                filename, lineno, column, message = line.split(":", 3)

                code = message.strip().split()[0]

                severity = (
                    "HIGH"
                    if code.startswith(("E9", "F"))
                    else "MEDIUM"
                )

                findings.append(
                    ResultParser.create_finding(
                        tool="Flake8",
                        file=filename,
                        line=int(lineno),
                        column=int(column),
                        message=message.strip(),
                        severity=severity,
                        rule=code,
                    )
                )

            except Exception:
                continue

        return findings

    @staticmethod
    def parse_pylint(data: list[dict]) -> list[Finding]:
        """
        Parse pylint JSON output.
        """

        findings = []

        for issue in data:

            findings.append(
                ResultParser.create_finding(
                    tool="Pylint",
                    file=issue.get("path", ""),
                    line=issue.get("line", 0),
                    column=issue.get("column", 0),
                    message=issue.get("message", ""),
                    severity=issue.get("type", "INFO"),
                    rule=issue.get("symbol"),
                )
            )

        return findings

    @staticmethod
    def parse_bandit(results: list[dict]) -> list[Finding]:
        """
        Parse Bandit JSON results.
        """

        findings = []

        for issue in results:

            findings.append(
                ResultParser.create_finding(
                    tool="Bandit",
                    file=issue.get("filename", ""),
                    line=issue.get("line_number", 0),
                    message=issue.get("issue_text", ""),
                    severity=issue.get("issue_severity", "LOW"),
                    rule=issue.get("test_id"),
                )
            )

        return findings

    @staticmethod
    def parse_semgrep(results: list[dict]) -> list[Finding]:
        """
        Parse Semgrep JSON results.
        """

        findings = []

        for issue in results:

            findings.append(
                ResultParser.create_finding(
                    tool="Semgrep",
                    file=issue["path"],
                    line=issue["start"]["line"],
                    message=issue["extra"]["message"],
                    severity=issue["extra"].get("severity", "MEDIUM"),
                    rule=issue["check_id"],
                )
            )

        return findings

    @staticmethod
    def parse_radon(
        *,
        file: str,
        message: str,
        line: int,
        complexity: int,
    ) -> Finding:
        """
        Convert Radon complexity result into Finding.
        """

        if complexity >= 20:
            severity = Severity.HIGH
        elif complexity >= 10:
            severity = Severity.MEDIUM
        else:
            severity = Severity.LOW

        return Finding(
            tool="Radon",
            file=file,
            line=line,
            column=0,
            message=message,
            severity=severity,
            rule=f"CC={complexity}",
        )

@staticmethod
def parse_bandit(results: list[dict]) -> list[Finding]:

    findings = []

    for issue in results:

        findings.append(
            ResultParser.create_finding(
                tool="Bandit",
                file=issue.get("filename", ""),
                line=issue.get("line_number", 0),
                column=0,
                message=issue.get("issue_text", ""),
                severity=issue.get(
                    "issue_severity",
                    "LOW",
                ),
                rule=issue.get("test_id"),
            )
        )

    return findings

@staticmethod
def parse_semgrep(
    results: list[dict],
) -> list[Finding]:

    findings = []

    for issue in results:

        extra = issue.get("extra", {})

        start = issue.get("start", {})

        findings.append(
            ResultParser.create_finding(
                tool="Semgrep",
                file=issue.get("path", ""),
                line=start.get("line", 0),
                column=start.get("col", 0),
                message=extra.get("message", ""),
                severity=extra.get(
                    "severity",
                    "INFO",
                ),
                rule=issue.get(
                    "check_id",
                    "",
                ),
            )
        )

    return findings