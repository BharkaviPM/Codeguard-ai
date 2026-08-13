from services.groq_service import GroqService


class SummaryAgent:

    @staticmethod
    def generate(
        security_review,
        code_review,
        remediation
    ):

        prompt = f"""
You are a Senior Engineering Reviewer.

Security Review:

{security_review}

Code Review:

{code_review}

Remediation:

{remediation}

Generate:

- Executive Summary
- Severity Breakdown
- Key Risks
- Recommended Actions
- Overall Code Health Score (0-100)

Format like a Pull Request review.
"""

        return GroqService.chat(prompt)