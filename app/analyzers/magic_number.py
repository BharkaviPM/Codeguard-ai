import ast


class MagicNumberAnalyzer:

    @staticmethod
    def analyze(tree):

        findings = []

        # Ignore common constants
        ignored_numbers = {0, 1, -1}

        for node in ast.walk(tree):

            if isinstance(node, ast.Constant):

                if isinstance(node.value, (int, float)):

                    if node.value not in ignored_numbers:

                        findings.append({

                            "agent": "Code Analysis",

                            "severity": "Low",

                            "title": "Magic Number",

                            "description":
                                f"Magic number '{node.value}' found.",

                            "line_number":
                                getattr(node, "lineno", 0),

                            "suggestion":
                                "Replace the magic number with a named constant."

                        })

        return findings