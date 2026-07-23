from __future__ import annotations

from app.agents.analysis.models import Finding, Severity


class FindingSorter:
    """
    Utility class for sorting findings.

    Default order:
        1. Severity
        2. File path
        3. Line number
        4. Tool
    """

    _SEVERITY_ORDER = {
        Severity.CRITICAL: 0,
        Severity.HIGH: 1,
        Severity.MEDIUM: 2,
        Severity.LOW: 3,
        Severity.INFO: 4,
    }

    @classmethod
    def by_severity(
        cls,
        findings: list[Finding],
    ) -> list[Finding]:
        """
        Sort findings by severity, then file, line, and tool.
        """

        return sorted(
            findings,
            key=lambda finding: (
                cls._SEVERITY_ORDER.get(
                    finding.severity,
                    99,
                ),
                finding.file,
                finding.line,
                finding.tool,
            ),
        )

    @staticmethod
    def by_file(
        findings: list[Finding],
    ) -> list[Finding]:
        """
        Sort findings alphabetically by file.
        """

        return sorted(
            findings,
            key=lambda finding: (
                finding.file,
                finding.line,
            ),
        )

    @staticmethod
    def by_tool(
        findings: list[Finding],
    ) -> list[Finding]:
        """
        Sort findings alphabetically by analyzer/tool.
        """

        return sorted(
            findings,
            key=lambda finding: (
                finding.tool,
                finding.file,
                finding.line,
            ),
        )

    @staticmethod
    def by_line(
        findings: list[Finding],
    ) -> list[Finding]:
        """
        Sort findings by file and line number.
        """

        return sorted(
            findings,
            key=lambda finding: (
                finding.file,
                finding.line,
            ),
        )