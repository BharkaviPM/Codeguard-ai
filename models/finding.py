from dataclasses import dataclass


@dataclass
class Finding:
    tool: str
    finding_type: str
    severity: str
    title: str
    description: str
    line_number: int
    recommendation: str