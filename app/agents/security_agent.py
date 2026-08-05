import ast
import re
import time

from app.services.groq_service import GroqService


class SecurityAgent:

    # -------------------------------------------------------
    # SQL Injection
    # -------------------------------------------------------

    @staticmethod
    def detect_sql_injection(code):

        findings = []

        patterns = [

            r"SELECT.*\+",

            r"INSERT.*\+",

            r"UPDATE.*\+",

            r"DELETE.*\+",

            r"execute\s*\(.+\+"

        ]

        lines = code.splitlines()

        for i, line in enumerate(lines):

            for pattern in patterns:

                if re.search(pattern, line, re.IGNORECASE):

                    findings.append({

                        "agent": "Security",

                        "severity": "Critical",

                        "title": "Possible SQL Injection",

                        "description":
                        "Dynamic SQL query detected.",

                        "line_number":
                        i + 1,

                        "suggestion":
                        "Use parameterized queries."

                    })

        return findings

    # -------------------------------------------------------
    # Unsafe eval()
    # -------------------------------------------------------

    @staticmethod
    def detect_eval(code):

        findings = []

        try:

            tree = ast.parse(code)

            for node in ast.walk(tree):

                if isinstance(node, ast.Call):

                    if isinstance(node.func, ast.Name):

                        if node.func.id == "eval":

                            findings.append({

                                "agent": "Security",

                                "severity": "Critical",

                                "title": "Unsafe eval()",

                                "description":
                                "eval() can execute arbitrary code.",

                                "line_number":
                                node.lineno,

                                "suggestion":
                                "Avoid eval()."

                            })

        except Exception:

            pass

        return findings

    # -------------------------------------------------------
    # Command Injection
    # -------------------------------------------------------

    @staticmethod
    def detect_command_injection(code):

        findings = []

        patterns = [

            r"os\.system",

            r"subprocess\.Popen",

            r"subprocess\.call",

            r"subprocess\.run"

        ]

        lines = code.splitlines()

        for i, line in enumerate(lines):

            for pattern in patterns:

                if re.search(pattern, line):

                    findings.append({

                        "agent": "Security",

                        "severity": "High",

                        "title": "Command Injection",

                        "description":
                        "Executing system commands.",

                        "line_number":
                        i + 1,

                        "suggestion":
                        "Avoid shell=True and validate user input."

                    })

        return findings

    # -------------------------------------------------------
    # Hardcoded Secrets
    # -------------------------------------------------------

    @staticmethod
    def detect_hardcoded_secrets(code):

        findings = []

        secret_patterns = [

            r'password\s*=\s*["\'].*["\']',

            r'api_key\s*=\s*["\'].*["\']',

            r'secret\s*=\s*["\'].*["\']',

            r'token\s*=\s*["\'].*["\']'

        ]

        lines = code.splitlines()

        for i, line in enumerate(lines):

            for pattern in secret_patterns:

                if re.search(pattern, line, re.IGNORECASE):

                    findings.append({

                        "agent": "Security",

                        "severity": "High",

                        "title": "Hardcoded Secret",

                        "description":
                        "Sensitive credential found in source code.",

                        "line_number":
                        i + 1,

                        "suggestion":
                        "Use environment variables or a secrets manager."

                    })

        return findings

    # -------------------------------------------------------
    # Path Traversal
    # -------------------------------------------------------

    @staticmethod
    def detect_path_traversal(code):

        findings = []

        lines = code.splitlines()

        for i, line in enumerate(lines):

            if "../" in line or "..\\" in line:

                findings.append({

                    "agent": "Security",

                    "severity": "Medium",

                    "title": "Path Traversal",

                    "description":
                    "Relative file path detected.",

                    "line_number":
                    i + 1,

                    "suggestion":
                    "Validate user supplied paths."

                })

        return findings

    # -------------------------------------------------------
    # AI Review
    # -------------------------------------------------------

    @staticmethod
    def ai_review(code):

        prompt = f"""
You are an OWASP Top 10 Security Expert.

Analyze the following source code.

Focus ONLY on security vulnerabilities.

Check for:

- SQL Injection
- XSS
- Command Injection
- Hardcoded Secrets
- Broken Authentication
- Broken Access Control
- Path Traversal
- Weak Cryptography
- Unsafe File Upload
- Insecure Deserialization
- Insecure Randomness
- Sensitive Data Exposure

Do not repeat obvious vulnerabilities already detected by static analysis.

Return a concise professional review.

Code:

{code}
"""

        return GroqService.chat(prompt)

    # -------------------------------------------------------
    # Main Analysis
    # -------------------------------------------------------

    @staticmethod
    def analyze(language, code):

        start = time.time()

        try:

            findings = []

            if language.lower() == "python":

                findings.extend(
                    SecurityAgent.detect_sql_injection(code)
                )

                findings.extend(
                    SecurityAgent.detect_eval(code)
                )

                findings.extend(
                    SecurityAgent.detect_command_injection(code)
                )

                findings.extend(
                    SecurityAgent.detect_hardcoded_secrets(code)
                )

                findings.extend(
                    SecurityAgent.detect_path_traversal(code)
                )

            elif language.lower() == "java":

                findings.extend(
                    SecurityAgent.detect_sql_injection(code)
                )

                findings.extend(
                    SecurityAgent.detect_hardcoded_secrets(code)
                )

                findings.extend(
                    SecurityAgent.detect_path_traversal(code)
                )

            critical = 0
            high = 0
            medium = 0
            low = 0

            for finding in findings:

                severity = finding["severity"].lower()

                if severity == "critical":
                    critical += 1

                elif severity == "high":
                    high += 1

                elif severity == "medium":
                    medium += 1

                elif severity == "low":
                    low += 1

            ai_review = SecurityAgent.ai_review(code)

            return {

                "agent": "Security",

                "status": "success",

                "total_findings": len(findings),

                "critical": critical,

                "high": high,

                "medium": medium,

                "low": low,

                "findings": findings,

                "ai_review": ai_review,

                "execution_time":
                round(time.time() - start, 2)

            }

        except Exception as e:

            return {

                "agent": "Security",

                "status": "error",

                "message": str(e),

                "total_findings": 0,

                "critical": 0,

                "high": 0,

                "medium": 0,

                "low": 0,

                "findings": [],

                "ai_review": "",

                "execution_time":
                round(time.time() - start, 2)

            }