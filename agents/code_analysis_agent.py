# agents/code_analysis_agent.py

from services.groq_service import GroqService


class CodeAnalysisAgent:

    @staticmethod
    def ai_review(code: str):

        prompt = f"""
You are a Principal Software Architect.

Review this code for:

- Code Smells
- Maintainability
- Readability
- Design Patterns
- SOLID Violations
- High Complexity
- Duplicate Logic
- Error Handling Issues
- Performance Issues

Return:

- Finding
- Severity
- Explanation
- Recommendation

Code:

{code}
"""

        return GroqService.chat(prompt)