from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Severity(str, Enum):
    INFO = "INFO"
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


@dataclass
class Finding:

    tool: str

    category: str

    title: str

    description: str

    severity: Severity

    file: str

    line: int | None = None

    column: int | None = None

    recommendation: str = ""

    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class AnalysisResult:

    analyzer: str

    findings: list[Finding] = field(default_factory=list)

    metrics: dict[str, Any] = field(default_factory=dict)

    execution_time: float = 0.0

    success: bool = True

    error: str | None = None