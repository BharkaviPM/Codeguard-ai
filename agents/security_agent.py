# agents/security_agent.py

from services.groq_service import GroqService


class SecurityAgent:

    @staticmethod
    def ai_review(code: str):

        prompt = f"""
You are a Senior Application Security Engineer.

Analyze the source code for security vulnerabilities.

Focus on:

- OWASP Top 10
- CWE vulnerabilities
- Authentication flaws
- Authorization flaws
- SQL Injection
- XSS
- CSRF
- SSRF
- Command Injection
- Hardcoded Secrets
- Insecure Cryptography
- Path Traversal
- File Upload Risks
- Sensitive Data Exposure

Rules:

1. Explain only real vulnerabilities.
2. Ignore style issues.
3. Provide severity.
4. Provide impacted code.
5. Provide remediation.

Code:

{code}
"""

        return GroqService.chat(prompt)