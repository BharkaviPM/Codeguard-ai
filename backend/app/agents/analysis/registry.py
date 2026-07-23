from __future__ import annotations

from app.analyzers.base import BaseAnalyzer


class AnalyzerRegistry:
    """
    Registry for all available analyzers.

    Responsibilities:
    - Register analyzers
    - Prevent duplicate registrations
    - Lookup analyzers
    - Filter analyzers by language
    """

    def __init__(self) -> None:
        self._analyzers: dict[str, BaseAnalyzer] = {}

    def register(
        self,
        analyzer: BaseAnalyzer,
    ) -> None:
        """
        Register a new analyzer.

        Raises:
            ValueError if analyzer is already registered.
        """

        key = analyzer.name.lower()

        if key in self._analyzers:
            raise ValueError(
                f"Analyzer '{analyzer.name}' is already registered."
            )

        self._analyzers[key] = analyzer

    def unregister(
        self,
        name: str,
    ) -> None:
        """
        Remove an analyzer.
        """

        self._analyzers.pop(name.lower(), None)

    def get(
        self,
        name: str,
    ) -> BaseAnalyzer | None:
        """
        Retrieve an analyzer by name.
        """

        return self._analyzers.get(name.lower())

    def exists(
        self,
        name: str,
    ) -> bool:
        """
        Check whether an analyzer exists.
        """

        return name.lower() in self._analyzers

    def get_all(
        self,
    ) -> list[BaseAnalyzer]:
        """
        Return every registered analyzer.
        """

        return list(self._analyzers.values())

    def get_supported(
        self,
        language: str,
    ) -> list[BaseAnalyzer]:
        """
        Return analyzers supporting the specified language.
        """

        language = language.lower()

        return [
            analyzer
            for analyzer in self._analyzers.values()
            if language in {
                lang.lower()
                for lang in analyzer.supported_languages
            }
        ]

    def clear(self) -> None:
        """
        Remove every registered analyzer.
        """

        self._analyzers.clear()

    def __len__(self) -> int:
        return len(self._analyzers)

    def __iter__(self):
        return iter(self._analyzers.values())