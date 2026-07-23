from __future__ import annotations

from app.agents.analysis.models import (
    AnalysisResult,
    Finding,
    Severity,
)
from app.agents.analysis.registry import AnalyzerRegistry
from app.agents.analysis.runner import AnalysisRunner
from app.analyzers.base import BaseAnalyzer


class DummyAnalyzer(BaseAnalyzer):
    """
    Dummy analyzer for testing.
    """

    name = "Dummy Analyzer"

    supported_languages = [
        "Python",
    ]

    def analyze(
        self,
        project_path: str,
    ) -> AnalysisResult:

        return AnalysisResult(
            analyzer=self.name,
            findings=[
                Finding(
                    tool="Dummy",
                    file="main.py",
                    line=1,
                    column=1,
                    severity=Severity.LOW,
                    rule="D001",
                    message="Dummy finding",
                )
            ],
            metrics={
                "files": 1,
            },
            execution_time=0.01,
        )


class FailingAnalyzer(BaseAnalyzer):
    """
    Analyzer that always raises an exception.
    """

    name = "Failing Analyzer"

    supported_languages = [
        "Python",
    ]

    def analyze(
        self,
        project_path: str,
    ):

        raise RuntimeError(
            "Analyzer failed"
        )


def test_runner_empty_registry():

    registry = AnalyzerRegistry()

    runner = AnalysisRunner(
        registry
    )

    results = runner.run(
        project_path=".",
        language="Python",
    )

    assert results == []


def test_runner_executes_single_analyzer():

    registry = AnalyzerRegistry()

    registry.register(
        DummyAnalyzer()
    )

    runner = AnalysisRunner(
        registry
    )

    results = runner.run(
        project_path=".",
        language="Python",
    )

    assert len(results) == 1

    assert (
        results[0].analyzer
        == "Dummy Analyzer"
    )


def test_runner_executes_multiple_analyzers():

    registry = AnalyzerRegistry()

    registry.register(
        DummyAnalyzer()
    )

    registry.register(
        DummyAnalyzer()
    )

    runner = AnalysisRunner(
        registry
    )

    results = runner.run(
        project_path=".",
        language="Python",
    )

    assert len(results) == 2


def test_runner_skips_wrong_language():

    registry = AnalyzerRegistry()

    registry.register(
        DummyAnalyzer()
    )

    runner = AnalysisRunner(
        registry
    )

    results = runner.run(
        project_path=".",
        language="Java",
    )

    assert results == []


def test_runner_handles_failure():

    registry = AnalyzerRegistry()

    registry.register(
        FailingAnalyzer()
    )

    runner = AnalysisRunner(
        registry
    )

    results = runner.run(
        project_path=".",
        language="Python",
    )

    assert results == []


def test_runner_returns_analysis_result():

    registry = AnalyzerRegistry()

    registry.register(
        DummyAnalyzer()
    )

    runner = AnalysisRunner(
        registry
    )

    results = runner.run(
        project_path=".",
        language="Python",
    )

    assert isinstance(
        results[0],
        AnalysisResult,
    )


def test_runner_returns_findings():

    registry = AnalyzerRegistry()

    registry.register(
        DummyAnalyzer()
    )

    runner = AnalysisRunner(
        registry
    )

    results = runner.run(
        project_path=".",
        language="Python",
    )

    assert len(
        results[0].findings
    ) == 1

    assert (
        results[0]
        .findings[0]
        .tool
        == "Dummy"
    )


def test_runner_returns_metrics():

    registry = AnalyzerRegistry()

    registry.register(
        DummyAnalyzer()
    )

    runner = AnalysisRunner(
        registry
    )

    results = runner.run(
        project_path=".",
        language="Python",
    )

    assert (
        results[0]
        .metrics["files"]
        == 1
    )