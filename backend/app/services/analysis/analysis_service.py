from app.agents.coordinator.coordinator import CoordinatorAgent

from app.findings.merger import FindingsMerger
from app.findings.severity import SeverityEngine


class AnalysisService:

    def __init__(self):

        self.coordinator = CoordinatorAgent()

    def analyze_project(
        self,
        project_path,
        language
    ):

        result = self.coordinator.analyze(
            project_path,
            language
        )

        findings = FindingsMerger.merge(

            result["analysis"],

            result["security"]

        )

        severity = SeverityEngine.summarize(
            findings
        )

        return {

            "summary": severity,

            "analysis": result["analysis"],

            "security": result["security"],

            "findings": findings

        }