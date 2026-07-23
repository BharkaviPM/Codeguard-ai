from __future__ import annotations

import logging
import time
from pathlib import Path

from app.agents.analysis.models import (
    AnalysisResult,
    Finding,
)
from app.agents.analysis.registry import AnalyzerRegistry
from app.agents.analysis.runner import AnalysisRunner

from app.analyzers.ast.analyzer import ASTAnalyzer

from app.services.analysis.radon_service import RadonAnalyzer
from app.services.analysis.flake8_service import Flake8Analyzer
from app.services.analysis.pylint_service import PylintAnalyzer

from app.services.security.bandit_service import BanditAnalyzer
from app.services.security.semgrep_service import SemgrepAnalyzer
from app.services.security.detect_secrets_service import (
    DetectSecretsAnalyzer,
)
from app.services.security.pip_audit_service import (
    PipAuditAnalyzer,
)

from app.findings.deduplicator import FindingDeduplicator
from app.findings.sorter import FindingSorter
from app.findings.statistics import FindingStatistics

logger = logging.getLogger(__name__)


class AnalysisAgent:
    """
    Main analysis coordinator.

    Responsibilities
    ----------------
    • Register analyzers
    • Execute analyzers
    • Merge findings
    • Deduplicate findings
    • Sort findings
    • Generate summary metrics
    """

    def __init__(self) -> None:

        self.registry = AnalyzerRegistry()

        self._register_default_analyzers()

        self.runner = AnalysisRunner(self.registry)

    # ----------------------------------------------------- #
    # Registration
    # ----------------------------------------------------- #

    def _register_default_analyzers(self) -> None:

        analyzers = [

            ASTAnalyzer(),

            RadonAnalyzer(),

            Flake8Analyzer(),

            PylintAnalyzer(),

            BanditAnalyzer(),

            SemgrepAnalyzer(),

            DetectSecretsAnalyzer(),

            PipAuditAnalyzer(),

        ]

        for analyzer in analyzers:

            self.registry.register(analyzer)

            logger.info(
                "Registered analyzer: %s",
                analyzer.name,
            )

    # ----------------------------------------------------- #
    # Public API
    # ----------------------------------------------------- #

    def analyze(
        self,
        project_path: str,
        language: str = "Python",
    ) -> AnalysisResult:

        logger.info(
            "Starting analysis for %s",
            project_path,
        )

        project = Path(project_path)

        if not project.exists():

            raise FileNotFoundError(project_path)

        start = time.perf_counter()

        analyzer_results = self.runner.run(
            project_path=project_path,
            language=language,
        )

        merged = AnalysisResult(
            analyzer="AnalysisAgent",
            findings=[],
            metrics={},
            execution_time=0.0,
        )

        #
        # Merge analyzer outputs
        #

        for result in analyzer_results:

            merged.findings.extend(
                result.findings
            )

            merged.metrics[
                result.analyzer
            ] = result.metrics

        #
        # Remove duplicates
        #

        merged.findings = (
            FindingDeduplicator.deduplicate(
                merged.findings
            )
        )

        #
        # Sort findings
        #

        merged.findings = (
            FindingSorter.by_severity(
                merged.findings
            )
        )

        #
        # Summary statistics
        #

        merged.metrics["summary"] = (
            self._build_summary(
                merged.findings,
                analyzer_results,
            )
        )

        merged.execution_time = round(
            time.perf_counter() - start,
            3,
        )

        logger.info(
            "Analysis completed (%d findings)",
            len(merged.findings),
        )

        return merged

    # ----------------------------------------------------- #
    # Summary Builder
    # ----------------------------------------------------- #

    def _build_summary(
        self,
        findings: list[Finding],
        results: list[AnalysisResult],
    ) -> dict:

        summary = FindingStatistics.summary(
            findings
        )

        summary["analyzers"] = len(results)

        return {

            **summary,

            "tool_statistics": (
                FindingStatistics.by_tool(
                    findings
                )
            ),

            "file_statistics": (
                FindingStatistics.by_file(
                    findings
                )
            ),

            "rule_statistics": (
                FindingStatistics.by_rule(
                    findings
                )
            ),

            "severity_statistics": (
                FindingStatistics.by_severity(
                    findings
                )
            ),

            "top_files": (
                FindingStatistics.top_files(
                    findings
                )
            ),

            "top_rules": (
                FindingStatistics.top_rules(
                    findings
                )
            ),
        }