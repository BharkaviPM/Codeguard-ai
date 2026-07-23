from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.agents.analysis.models import AnalysisResult


class BaseAnalyzer(ABC):

    name = ""

    supported_languages = []

    @abstractmethod
    def analyze(
        self,
        project_path: str
    ) -> AnalysisResult:
        pass