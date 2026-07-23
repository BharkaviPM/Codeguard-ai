from __future__ import annotations

from pathlib import Path

import pytest

from app.agents.analysis.agent import AnalysisAgent
from app.agents.analysis.models import (
    AnalysisResult,
)


def test_invalid_project():

    agent = AnalysisAgent()

    with pytest.raises(
        FileNotFoundError
    ):

        agent.analyze(
            "does_not_exist"
        )


def test_analysis_returns_result(
    tmp_path: Path,
):

    project = tmp_path / "project"

    project.mkdir()

    (
        project / "main.py"
    ).write_text(
        "print('Hello World')"
    )

    agent = AnalysisAgent()

    result = agent.analyze(
        str(project)
    )

    assert isinstance(
        result,
        AnalysisResult,
    )


def test_execution_time(
    tmp_path: Path,
):

    project = tmp_path / "project"

    project.mkdir()

    (
        project / "main.py"
    ).write_text(
        "print('Hello')"
    )

    agent = AnalysisAgent()

    result = agent.analyze(
        str(project)
    )

    assert (
        result.execution_time
        >= 0
    )


def test_summary_exists(
    tmp_path: Path,
):

    project = tmp_path / "project"

    project.mkdir()

    (
        project / "main.py"
    ).write_text(
        "print('Test')"
    )

    agent = AnalysisAgent()

    result = agent.analyze(
        str(project)
    )

    assert (
        "summary"
        in result.metrics
    )


def test_summary_fields(
    tmp_path: Path,
):

    project = tmp_path / "project"

    project.mkdir()

    (
        project / "main.py"
    ).write_text(
        "x = 1"
    )

    agent = AnalysisAgent()

    result = agent.analyze(
        str(project)
    )

    summary = result.metrics[
        "summary"
    ]

    assert (
        "analyzers"
        in summary
    )

    assert (
        "total_findings"
        in summary
    )

    assert (
        "critical"
        in summary
    )

    assert (
        "high"
        in summary
    )

    assert (
        "medium"
        in summary
    )

    assert (
        "low"
        in summary
    )

    assert (
        "info"
        in summary
    )


def test_statistics_exist(
    tmp_path: Path,
):

    project = tmp_path / "project"

    project.mkdir()

    (
        project / "main.py"
    ).write_text(
        "print('Statistics')"
    )

    agent = AnalysisAgent()

    result = agent.analyze(
        str(project)
    )

    summary = result.metrics[
        "summary"
    ]

    assert (
        "tool_statistics"
        in summary
    )

    assert (
        "file_statistics"
        in summary
    )

    assert (
        "rule_statistics"
        in summary
    )

    assert (
        "severity_statistics"
        in summary
    )

    assert (
        "top_files"
        in summary
    )

    assert (
        "top_rules"
        in summary
    )


def test_findings_is_list(
    tmp_path: Path,
):

    project = tmp_path / "project"

    project.mkdir()

    (
        project / "main.py"
    ).write_text(
        "print('Findings')"
    )

    agent = AnalysisAgent()

    result = agent.analyze(
        str(project)
    )

    assert isinstance(
        result.findings,
        list,
    )


def test_metrics_is_dict(
    tmp_path: Path,
):

    project = tmp_path / "project"

    project.mkdir()

    (
        project / "main.py"
    ).write_text(
        "print('Metrics')"
    )

    agent = AnalysisAgent()

    result = agent.analyze(
        str(project)
    )

    assert isinstance(
        result.metrics,
        dict,
    )


def test_analyzer_metrics_exist(
    tmp_path: Path,
):

    project = tmp_path / "project"

    project.mkdir()

    (
        project / "main.py"
    ).write_text(
        "print('Agent')"
    )

    agent = AnalysisAgent()

    result = agent.analyze(
        str(project)
    )

    assert len(
        result.metrics
    ) >= 1
    