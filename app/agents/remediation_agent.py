import time

from app.services.groq_service import GroqService


class RemediationAgent:

    @staticmethod
    def generate_fix(
        language,
        code,
        findings
    ):

        start_time = time.time()

        try:

            findings_text = ""

            if isinstance(findings, list):

                for finding in findings:

                    findings_text += f"""
Title : {finding.get('title')}

Severity : {finding.get('severity')}

Description : {finding.get('description')}

Suggestion : {finding.get('suggestion')}

"""

            prompt = f"""
You are a Senior Security Engineer and Code Reviewer.

Language:
{language}

Original Code:

{code}

Detected Issues:

{findings_text}

Tasks:

1. Explain every issue.

2. Show why it is dangerous.

3. Rewrite the complete code.

4. Apply all fixes.

5. Follow OWASP Secure Coding.

6. Improve readability.

7. Improve performance.

Return in markdown format.
"""

            remediation = GroqService.chat(prompt)

            return {

                "agent": "Remediation",

                "status": "success",

                "language": language,

                "total_issues_fixed": len(findings),

                "result": remediation,

                "execution_time": round(
                    time.time() - start_time,
                    2
                )

            }

        except Exception as e:

            return {

                "agent": "Remediation",

                "status": "error",

                "language": language,

                "total_issues_fixed": 0,

                "message": str(e),

                "result": "",

                "execution_time": round(
                    time.time() - start_time,
                    2
                )

            }