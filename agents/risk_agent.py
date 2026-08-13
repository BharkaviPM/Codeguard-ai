from services.groq_service import GroqService


class RiskAgent:

    def analyze(
        self,
        security_review,
        code_review,
        performance_review
    ):

        prompt = f"""
You are a Chief Security Architect.

Analyze the reports below and provide:

1. Overall Risk Score (0-100)
2. Security Score
3. Code Quality Score
4. Performance Score
5. Compliance Status
6. Approval Decision
7. Final Recommendation

Security Review:
{security_review}

Code Review:
{code_review}

Performance Review:
{performance_review}
"""

        return GroqService.chat(prompt)