from agents.code_analysis_agent import CodeAnalysisAgent
from agents.security_agent import SecurityAgent
from agents.remediation_agent import RemediationAgent
from agents.summary_agent import SummaryAgent

try:
    from agents.performance_agent import PerformanceAgent
    PERFORMANCE_AVAILABLE = True
except Exception:
    PERFORMANCE_AVAILABLE = False

try:
    from agents.risk_agent import RiskAgent
    RISK_AVAILABLE = True
except Exception:
    RISK_AVAILABLE = False


class ReviewWorkflow:

    def __init__(self):

        self.code_agent = CodeAnalysisAgent()
        self.security_agent = SecurityAgent()
        self.remediation_agent = RemediationAgent()
        self.summary_agent = SummaryAgent()

        self.performance_agent = None
        self.risk_agent = None

        if PERFORMANCE_AVAILABLE:
            self.performance_agent = PerformanceAgent()

        if RISK_AVAILABLE:
            self.risk_agent = RiskAgent()

    def run(self, code):

        # ==========================================
        # CODE REVIEW
        # ==========================================

        try:
            code_review = self.code_agent.ai_review(code)
        except Exception as e:
            code_review = f"Code Review Error:\n{str(e)}"

        # ==========================================
        # SECURITY REVIEW
        # ==========================================

        try:
            security_review = self.security_agent.ai_review(code)
        except Exception as e:
            security_review = f"Security Review Error:\n{str(e)}"

        # ==========================================
        # PERFORMANCE REVIEW
        # ==========================================

        performance_review = "Performance analysis not available."

        if self.performance_agent:

            try:
                performance_review = (
                    self.performance_agent.ai_review(code)
                )

            except Exception as e:

                performance_review = (
                    f"Performance Review Error:\n{str(e)}"
                )

        # ==========================================
        # REMEDIATION
        # ==========================================

        try:

            remediation = (
                self.remediation_agent.generate(
                    code,
                    security_review,
                    code_review
                )
            )

        except Exception as e:

            remediation = (
                f"Remediation Error:\n{str(e)}"
            )

        # ==========================================
        # RISK ASSESSMENT
        # ==========================================

        risk_report = "Risk analysis not available."

        if self.risk_agent:

            try:

                risk_report = (
                    self.risk_agent.analyze(
                        security_review,
                        code_review,
                        performance_review
                    )
                )

            except Exception as e:

                risk_report = (
                    f"Risk Assessment Error:\n{str(e)}"
                )

        # ==========================================
        # SUMMARY
        # ==========================================

        try:

            final_report = (
                self.summary_agent.generate(
                    security_review,
                    code_review,
                    remediation
                )
            )

        except Exception as e:

            final_report = (
                f"Summary Error:\n{str(e)}"
            )

        # ==========================================
        # RETURN RESULTS
        # ==========================================

        return {

            "security_review": security_review,

            "code_review": code_review,

            "performance_review": performance_review,

            "remediation": remediation,

            "risk_report": risk_report,

            "summary": final_report

        }