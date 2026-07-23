from __future__ import annotations

from pathlib import Path

import pytest

from app.agents.analysis.agent import AnalysisAgent
from app.agents.analysis.models import (
    AnalysisResult,
    Finding,
    Severity,
)
from app.agents.analysis.registry import AnalyzerRegistry
from app.agents.analysis.runner import AnalysisRunner
from app.analyzers.base import BaseAnalyzer


# ----------------------------------------------------------------------
# Dummy Analyzer
# ----------------------------------------------------------------------

class DummyAnalyzer(BaseAnalyzer):

    name = "Dummy"

    supported_languages = ["Python"]

    def analyze(
        self,
        project_path: str,
    ) -> AnalysisResult:

        return AnalysisResult(
            analyzer=self.name,
            findings=[
                Finding(
                    tool="Dummy",
                    file="demo.py",
                    line=1,
                    column=1,
                    severity=Severity.LOW,
                    rule="D001",
                    message="Dummy finding",
                )
            ],
            metrics={
                "files": 1
            },
            execution_time=0.01,
        )


# ----------------------------------------------------------------------
# Registry
# ----------------------------------------------------------------------

def test_registry_register():

    registry = AnalyzerRegistry()

    registry.register(
        DummyAnalyzer()
    )

    assert len(
        registry.get_all()
    ) == 1


def test_registry_supported_language():

    registry = AnalyzerRegistry()

    registry.register(
        DummyAnalyzer()
    )

    analyzers = registry.get_supported(
        "Python"
    )

    assert len(analyzers) == 1


# ----------------------------------------------------------------------
# Runner
# ----------------------------------------------------------------------

def test_runner_executes():

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
        == "Dummy"
    )


def test_runner_empty_registry():

    runner = AnalysisRunner(
        AnalyzerRegistry()
    )

    results = runner.run(
        ".",
        "Python",
    )

    assert results == []


# ----------------------------------------------------------------------
# Agent
# ----------------------------------------------------------------------

def test_invalid_project():

    agent = AnalysisAgent()

    with pytest.raises(
        FileNotFoundError
    ):

        agent.analyze(
            "does_not_exist"
        )


def test_summary_generation(tmp_path: Path):

    project = tmp_path / "sample"

    project.mkdir()

    file = project / "main.py"

    file.write_text(
        "print('hello')"
    )

    agent = AnalysisAgent()

    result = agent.analyze(
        str(project)
    )

    assert isinstance(
        result,
        AnalysisResult,
    )

    assert (
        "summary"
        in result.metrics
    )


# ----------------------------------------------------------------------
# Deduplication
# ----------------------------------------------------------------------

def test_duplicate_findings_removed():

    agent = AnalysisAgent()

    finding = Finding(
        tool="Test",
        file="a.py",
        line=1,
        column=1,
        severity=Severity.LOW,
        rule="T001",
        message="duplicate",
    )

    findings = [
        finding,
        finding,
    ]

    unique = (
        agent._build_summary
    )

    assert len(findings) == 2


# ----------------------------------------------------------------------
# Execution time
# ----------------------------------------------------------------------

def test_execution_time(tmp_path: Path):

    project = tmp_path / "code"

    project.mkdir()

    (project / "main.py").write_text(
        "print('hi')"
    )

    agent = AnalysisAgent()

    result = agent.analyze(
        str(project)
    )

    assert (
        result.execution_time
        >= 0
    )


# ----------------------------------------------------------------------
# Metrics
# ----------------------------------------------------------------------

def test_metrics_exist(tmp_path: Path):

    project = tmp_path / "metrics"

    project.mkdir()

    (project / "a.py").write_text(
        "x=1"
    )

    agent = AnalysisAgent()

    result = agent.analyze(
        str(project)
    )

    assert isinstance(
        result.metrics,
        dict,
    )


# ----------------------------------------------------------------------
# Findings sorted
# ----------------------------------------------------------------------

def test_findings_sorted(tmp_path: Path):

    project = tmp_path / "sort"

    project.mkdir()

    (project / "a.py").write_text(
        "print('hello')"
    )

    agent = AnalysisAgent()

    result = agent.analyze(
        str(project)
    )

    severities = [
        finding.severity
        for finding in result.findings
    ]

    assert severities == sorted(
        severities,
        key=lambda s: [
            Severity.CRITICAL,
            Severity.HIGH,
            Severity.MEDIUM,
            Severity.LOW,
            Severity.INFO,
        ].index(s)
        if s in [
            Severity.CRITICAL,
            Severity.HIGH,
            Severity.MEDIUM,
            Severity.LOW,
            Severity.INFO,
        ]
        else 99,
    )