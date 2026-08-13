from services.groq_service import GroqService


class PerformanceAgent:

    def ai_review(self, code):

        prompt = f"""
You are a Senior Performance Engineer.

Analyze this code for:

1. Time Complexity
2. Space Complexity
3. Slow Loops
4. Nested Loops
5. Database Query Efficiency
6. Memory Leaks
7. Scalability Issues
8. Performance Improvements

Provide:

- Findings
- Severity
- Recommendations
- Optimized Code Suggestions

Code:

{code}
"""

        return GroqService.chat(prompt)