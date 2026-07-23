from __future__ import annotations

import logging
import time
from concurrent.futures import (
    ThreadPoolExecutor,
    TimeoutError,
    as_completed,
)

from app.agents.analysis.models import AnalysisResult
from app.agents.analysis.registry import AnalyzerRegistry
from app.analyzers.base import BaseAnalyzer

logger = logging.getLogger(__name__)


class AnalysisRunner:
    """
    Executes all registered analyzers.

    Features
    --------
    • Parallel execution
    • Analyzer isolation
    • Timeout handling
    • Execution statistics
    • Failure recovery
    """

    def __init__(
        self,
        registry: AnalyzerRegistry,
        max_workers: int = 4,
        timeout: int = 300,
    ) -> None:

        self.registry = registry
        self.max_workers = max_workers
        self.timeout = timeout

    def _run_single(
        self,
        analyzer: BaseAnalyzer,
        project_path: str,
    ) -> AnalysisResult:
        """
        Execute a single analyzer.
        """

        logger.info(
            "Running analyzer: %s",
            analyzer.name,
        )

        start = time.perf_counter()

        result = analyzer.analyze(project_path)

        if not result.execution_time:

            result.execution_time = round(
                time.perf_counter() - start,
                3,
            )

        logger.info(
            "%s completed in %.3fs",
            analyzer.name,
            result.execution_time,
        )

        return result

    def run(
        self,
        project_path: str,
        language: str,
    ) -> list[AnalysisResult]:
        """
        Execute every analyzer supporting
        the requested language.
        """

        analyzers = self.registry.get_supported(
            language
        )

        if not analyzers:

            logger.warning(
                "No analyzers registered for language '%s'",
                language,
            )

            return []

        logger.info(
            "Executing %d analyzers",
            len(analyzers),
        )

        overall_start = time.perf_counter()

        results: list[AnalysisResult] = []

        success = 0
        failed = 0

        with ThreadPoolExecutor(
            max_workers=self.max_workers
        ) as executor:

            future_map = {

                executor.submit(
                    self._run_single,
                    analyzer,
                    project_path,
                ): analyzer

                for analyzer in analyzers

            }

            for future in as_completed(future_map):

                analyzer = future_map[future]

                try:

                    result = future.result(
                        timeout=self.timeout
                    )

                    results.append(result)

                    success += 1

                except TimeoutError:

                    failed += 1

                    logger.error(
                        "%s timed out after %ss",
                        analyzer.name,
                        self.timeout,
                    )

                except Exception:

                    failed += 1

                    logger.exception(
                        "%s failed during execution",
                        analyzer.name,
                    )

        results.sort(
            key=lambda item: item.analyzer
        )

        elapsed = round(
            time.perf_counter() - overall_start,
            3,
        )

        logger.info(
            (
                "Analysis completed "
                "(success=%d failed=%d "
                "time=%.3fs)"
            ),
            success,
            failed,
            elapsed,
        )

        return results