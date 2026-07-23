from __future__ import annotations

import pytest

from app.agents.analysis.registry import AnalyzerRegistry
from app.analyzers.base import BaseAnalyzer


class DummyAnalyzer(BaseAnalyzer):
    """
    Dummy analyzer used for testing.
    """

    name = "Dummy Analyzer"

    supported_languages = [
        "Python",
    ]

    def analyze(self, project_path: str):
        return None


def test_registry_initially_empty():

    registry = AnalyzerRegistry()

    assert len(registry) == 0
    assert registry.get_all() == []


def test_register_analyzer():

    registry = AnalyzerRegistry()

    analyzer = DummyAnalyzer()

    registry.register(analyzer)

    assert len(registry) == 1

    assert registry.exists(
        analyzer.name
    )


def test_get_analyzer():

    registry = AnalyzerRegistry()

    analyzer = DummyAnalyzer()

    registry.register(analyzer)

    result = registry.get(
        analyzer.name
    )

    assert result is analyzer


def test_get_unknown_analyzer():

    registry = AnalyzerRegistry()

    assert (
        registry.get("Unknown")
        is None
    )


def test_supported_language():

    registry = AnalyzerRegistry()

    analyzer = DummyAnalyzer()

    registry.register(analyzer)

    supported = registry.get_supported(
        "Python"
    )

    assert len(supported) == 1

    assert supported[0].name == analyzer.name


def test_unsupported_language():

    registry = AnalyzerRegistry()

    analyzer = DummyAnalyzer()

    registry.register(analyzer)

    supported = registry.get_supported(
        "Java"
    )

    assert supported == []


def test_unregister():

    registry = AnalyzerRegistry()

    analyzer = DummyAnalyzer()

    registry.register(analyzer)

    registry.unregister(
        analyzer.name
    )

    assert len(registry) == 0

    assert (
        registry.get(analyzer.name)
        is None
    )


def test_clear_registry():

    registry = AnalyzerRegistry()

    registry.register(
        DummyAnalyzer()
    )

    registry.clear()

    assert len(registry) == 0

    assert registry.get_all() == []


def test_duplicate_registration():

    registry = AnalyzerRegistry()

    analyzer = DummyAnalyzer()

    registry.register(analyzer)

    with pytest.raises(
        ValueError
    ):

        registry.register(analyzer)