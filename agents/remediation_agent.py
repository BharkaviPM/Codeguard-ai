from services.groq_service import GroqService


class RemediationAgent:

    @staticmethod
    def generate(
        code,
        security_review,
        code_review
    ):

        prompt = f"""
You are a Secure Coding Expert.

Source Code:

{code}

Security Review:

{security_review}

Code Review:

{code_review}

Generate:

1. Issue Explanation
2. Risk Impact
3. Fix Recommendation
4. Corrected Code Example
5. Best Practice Reference

Keep response structured.
"""

        return GroqService.chat(prompt)