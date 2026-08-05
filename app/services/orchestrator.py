from app.agents.code_agent import CodeAnalysisAgent
from app.agents.security_agent import SecurityAgent
from app.agents.remediation_agent import RemediationAgent
from app.agents.summary_agent import SummaryAgent


class Orchestrator:

    @staticmethod
    def analyze(language, code, filename="uploaded_file"):

        # ------------------------------------
        # Code Analysis
        # ------------------------------------

        code_analysis = CodeAnalysisAgent.analyze(
            language,
            code
        )

        # ------------------------------------
        # Security Analysis
        # ------------------------------------

        security = SecurityAgent.analyze(
            language,
            code
        )

        # ------------------------------------
        # Merge Findings
        # ------------------------------------

        findings = []

        findings.extend(
            code_analysis["findings"]
        )

        findings.extend(
            security["findings"]
        )

        # ------------------------------------
        # Remediation
        # ------------------------------------

        remediation = RemediationAgent.generate_fix(

            language,

            code,

            findings

        )

        # ------------------------------------
        # Summary
        # ------------------------------------

        summary = SummaryAgent.generate_summary(

            language,

            code,

            findings,

            remediation["result"]

        )

        # ------------------------------------
        # Final Response
        # ------------------------------------

        return {

            "project": {

                "filename": filename,

                "language": language,

                "lines_of_code": len(code.splitlines())

            },

            "code_analysis": code_analysis,

            "security": security,

            "remediation": remediation,

            "summary": summary

        }