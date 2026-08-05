import time

from app.services.groq_service import GroqService


class SummaryAgent:

    @staticmethod
    def calculate_score(findings):

        score = 100

        for finding in findings:

            severity = finding.get("severity", "").lower()

            if severity == "critical":
                score -= 25

            elif severity == "high":
                score -= 15

            elif severity == "medium":
                score -= 8

            elif severity == "low":
                score -= 3

        return max(score, 0)

    @staticmethod
    def severity_breakdown(findings):

        breakdown = {
            "Critical": 0,
            "High": 0,
            "Medium": 0,
            "Low": 0
        }

        for finding in findings:

            severity = finding.get("severity", "")

            if severity in breakdown:
                breakdown[severity] += 1

        return breakdown

    @staticmethod
    def generate_summary(

            language,
            code,
            findings,
            remediation

    ):

        start_time = time.time()

        try:

            health_score = SummaryAgent.calculate_score(findings)

            severity = SummaryAgent.severity_breakdown(findings)

            findings_text = ""

            for finding in findings:

                findings_text += f"""
Title : {finding.get("title")}
Severity : {finding.get("severity")}
Description : {finding.get("description")}
Suggestion : {finding.get("suggestion")}

"""

            prompt = f"""
You are a Senior Pull Request Reviewer.

Generate a professional Pull Request Review.

Language:
{language}

================================================

Code Health Score

{health_score}/100

================================================

Severity Breakdown

{severity}

================================================

Detected Findings

{findings_text}

================================================

Remediation

{remediation}

================================================

Generate:

1. Executive Summary

2. Code Quality Summary

3. Security Summary

4. Priority Fixes

5. Risk Assessment

6. Overall Recommendation

Keep the report concise and professional.

"""

            ai_summary = GroqService.chat(prompt)

            return {

                "agent": "PR Summary",

                "status": "success",

                "health_score": health_score,

                "severity": severity,

                "summary": ai_summary,

                "execution_time":
                    round(
                        time.time() - start_time,
                        2
                    )

            }

        except Exception as e:

            return {

                "agent": "PR Summary",

                "status": "error",

                "message": str(e),

                "health_score": 0,

                "severity": {

                    "Critical": 0,

                    "High": 0,

                    "Medium": 0,

                    "Low": 0

                },

                "summary": "",

                "execution_time":
                    round(
                        time.time() - start_time,
                        2
                    )

            }