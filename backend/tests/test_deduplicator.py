from app.findings.deduplicator import FindingDeduplicator
from app.agents.analysis.models import Finding, Severity


def test_empty_findings():

    assert (
        FindingDeduplicator.deduplicate([])
        == []
    )


def test_remove_duplicates():

    finding = Finding(
        tool="Bandit",
        file="app.py",
        line=10,
        column=1,
        severity=Severity.HIGH,
        rule="B101",
        message="Duplicate"
    )

    findings = [
        finding,
        finding,
    ]

    result = FindingDeduplicator.deduplicate(
        findings
    )

    assert len(result) == 1


def test_unique_findings():

    findings = [
        Finding(
            tool="Bandit",
            file="a.py",
            line=1,
            column=1,
            severity=Severity.HIGH,
            rule="B101",
            message="One",
        ),
        Finding(
            tool="Flake8",
            file="b.py",
            line=2,
            column=1,
            severity=Severity.LOW,
            rule="F401",
            message="Two",
        ),
    ]

    result = FindingDeduplicator.deduplicate(
        findings
    )

    assert len(result) == 2


def test_duplicate_count():

    findings = [
        Finding(
            tool="Bandit",
            file="app.py",
            line=1,
            column=1,
            severity=Severity.HIGH,
            rule="B101",
            message="Test",
        ),
        Finding(
            tool="Bandit",
            file="app.py",
            line=1,
            column=1,
            severity=Severity.HIGH,
            rule="B101",
            message="Test",
        ),
    ]

    assert (
        FindingDeduplicator.count_duplicates(
            findings
        )
        == 1
    )