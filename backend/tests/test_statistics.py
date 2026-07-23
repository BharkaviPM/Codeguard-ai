from app.findings.statistics import FindingStatistics
from app.agents.analysis.models import Finding, Severity


findings = [
    Finding(
        tool="Bandit",
        file="app.py",
        line=10,
        column=1,
        severity=Severity.HIGH,
        rule="B101",
        message="Issue 1",
    ),
    Finding(
        tool="Flake8",
        file="main.py",
        line=20,
        column=1,
        severity=Severity.LOW,
        rule="F401",
        message="Issue 2",
    ),
]


def test_summary():

    summary = FindingStatistics.summary(
        findings
    )

    assert (
        summary["total_findings"]
        == 2
    )


def test_by_tool():

    stats = FindingStatistics.by_tool(
        findings
    )

    assert "Bandit" in stats


def test_by_file():

    stats = FindingStatistics.by_file(
        findings
    )

    assert "app.py" in stats


def test_by_rule():

    stats = FindingStatistics.by_rule(
        findings
    )

    assert "B101" in stats


def test_by_severity():

    stats = FindingStatistics.by_severity(
        findings
    )

    assert (
        Severity.HIGH.name
        in stats
    )


def test_top_files():

    top = FindingStatistics.top_files(
        findings
    )

    assert len(top) > 0


def test_top_rules():

    top = FindingStatistics.top_rules(
        findings
    )

    assert len(top) > 0