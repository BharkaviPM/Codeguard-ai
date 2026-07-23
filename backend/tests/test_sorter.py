from app.findings.sorter import FindingSorter
from app.agents.analysis.models import Finding, Severity


findings = [
    Finding(
        tool="Flake8",
        file="b.py",
        line=20,
        column=1,
        severity=Severity.LOW,
        rule="F401",
        message="Unused import",
    ),
    Finding(
        tool="Bandit",
        file="a.py",
        line=5,
        column=1,
        severity=Severity.CRITICAL,
        rule="B101",
        message="Security issue",
    ),
]


def test_sort_by_severity():

    result = FindingSorter.by_severity(
        findings
    )

    assert (
        result[0].severity
        == Severity.CRITICAL
    )


def test_sort_by_file():

    result = FindingSorter.by_file(
        findings
    )

    assert result[0].file == "a.py"


def test_sort_by_tool():

    result = FindingSorter.by_tool(
        findings
    )

    assert result[0].tool == "Bandit"


def test_sort_by_line():

    result = FindingSorter.by_line(
        findings
    )

    assert result[0].line == 5