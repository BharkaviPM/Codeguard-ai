import time

from app.analyzers.python_analyzer import PythonAnalyzer
from app.analyzers.java_analyzer import JavaAnalyzer
from app.services.groq_service import GroqService


class CodeAnalysisAgent:

    @staticmethod
    def analyze(language, code):

        start_time = time.time()

        try:
            # -------------------------
            # Static Analysis
            # -------------------------

            if language.lower() == "python":
                findings = PythonAnalyzer.analyze(code)

            elif language.lower() == "java":
                findings = JavaAnalyzer.analyze(code)

            else:
                return {
                    "agent": "Code Analysis",
                    "status": "error",
                    "message": f"Unsupported language: {language}",
                    "total_findings": 0,
                    "critical": 0,
                    "high": 0,
                    "medium": 0,
                    "low": 0,
                    "findings": [],
                    "ai_review": "",
                    "execution_time": round(time.time() - start_time, 2)
                }

            # -------------------------
            # Severity Counts
            # -------------------------

            critical = 0
            high = 0
            medium = 0
            low = 0

            for finding in findings:

                severity = finding.get(
                    "severity",
                    ""
                ).lower()

                if severity == "critical":
                    critical += 1

                elif severity == "high":
                    high += 1

                elif severity == "medium":
                    medium += 1

                elif severity == "low":
                    low += 1

            # -------------------------
            # Groq AI Review
            # -------------------------

            prompt = f"""
You are a Senior Software Code Reviewer.

Analyze the following {language} code.

Focus ONLY on code quality.

Check for:

- Code smells
- Poor naming
- Complexity
- Maintainability
- Readability
- Duplicate logic
- Bad design patterns
- Missing validation
- Error handling
- Best practice violations

Do NOT repeat obvious issues already detected
by static analysis.

Code:

{code}

Provide concise developer-friendly recommendations.
"""

            ai_review = GroqService.chat(prompt)

            # -------------------------
            # Execution Time
            # -------------------------

            execution_time = round(
                time.time() - start_time,
                2
            )

            # -------------------------
            # Final Response
            # -------------------------

            return {
                "agent": "Code Analysis",
                "status": "success",
                "total_findings": len(findings),
                "critical": critical,
                "high": high,
                "medium": medium,
                "low": low,
                "findings": findings,
                "ai_review": ai_review,
                "execution_time": execution_time
            }

        except Exception as e:

            return {
                "agent": "Code Analysis",
                "status": "error",
                "message": str(e),
                "total_findings": 0,
                "critical": 0,
                "high": 0,
                "medium": 0,
                "low": 0,
                "findings": [],
                "ai_review": "",
                "execution_time": round(
                    time.time() - start_time,
                    2
                )
            }