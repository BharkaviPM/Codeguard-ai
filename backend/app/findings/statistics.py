from __future__ import annotations

from collections import Counter

from app.agents.analysis.models import Finding, Severity


class FindingStatistics:
    """
    Utility class for generating statistics from findings.
    """

    @staticmethod
    def summary(
        findings: list[Finding],
    ) -> dict:
        """
        Generate overall statistics.

        Returns
        -------
        {
            "total_findings": int,
            "critical": int,
            "high": int,
            "medium": int,
            "low": int,
            "info": int
        }
        """

        severity_counter = Counter(
            finding.severity
            for finding in findings
        )

        return {
            "total_findings": len(findings),
            "critical": severity_counter.get(
                Severity.CRITICAL,
                0,
            ),
            "high": severity_counter.get(
                Severity.HIGH,
                0,
            ),
            "medium": severity_counter.get(
                Severity.MEDIUM,
                0,
            ),
            "low": severity_counter.get(
                Severity.LOW,
                0,
            ),
            "info": severity_counter.get(
                Severity.INFO,
                0,
            ),
        }

    @staticmethod
    def by_tool(
        findings: list[Finding],
    ) -> dict[str, int]:
        """
        Count findings produced by each analyzer.
        """

        counter = Counter(
            finding.tool
            for finding in findings
        )

        return dict(
            sorted(counter.items())
        )

    @staticmethod
    def by_file(
        findings: list[Finding],
    ) -> dict[str, int]:
        """
        Count findings per file.
        """

        counter = Counter(
            finding.file
            for finding in findings
        )

        return dict(
            sorted(counter.items())
        )

    @staticmethod
    def by_rule(
        findings: list[Finding],
    ) -> dict[str, int]:
        """
        Count occurrences of every rule.
        """

        counter = Counter(
            finding.rule or "Unknown"
            for finding in findings
        )

        return dict(
            sorted(counter.items())
        )

    @staticmethod
    def by_severity(
        findings: list[Finding],
    ) -> dict[str, int]:
        """
        Return severity distribution.
        """

        counter = Counter(
            finding.severity.value
            for finding in findings
        )

        return dict(
            sorted(counter.items())
        )

    @staticmethod
    def top_files(
        findings: list[Finding],
        limit: int = 10,
    ) -> list[tuple[str, int]]:
        """
        Return files with the most findings.
        """

        counter = Counter(
            finding.file
            for finding in findings
        )

        return counter.most_common(limit)

    @staticmethod
    def top_rules(
        findings: list[Finding],
        limit: int = 10,
    ) -> list[tuple[str, int]]:
        """
        Return most common rules.
        """

        counter = Counter(
            finding.rule or "Unknown"
            for finding in findings
        )

        return counter.most_common(limit)