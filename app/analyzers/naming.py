import ast
import re


class NamingAnalyzer:

    snake_case = re.compile(r"^[a-z_][a-z0-9_]*$")

    @staticmethod
    def analyze(tree):

        findings = []

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                if not NamingAnalyzer.snake_case.match(node.name):

                    findings.append({

                        "agent": "Code Analysis",

                        "severity": "Low",

                        "title": "Naming Convention",

                        "description":
                            f"Function '{node.name}' should use snake_case.",

                        "line_number":
                            node.lineno,

                        "suggestion":
                            "Rename the function using snake_case."

                    })

        return findings