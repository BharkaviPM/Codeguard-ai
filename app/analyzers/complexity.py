import ast


class ComplexityAnalyzer:

    @staticmethod
    def analyze(tree):

        findings = []

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                complexity = 1

                for child in ast.walk(node):

                    if isinstance(
                        child,
                        (
                            ast.If,
                            ast.For,
                            ast.While,
                            ast.Try,
                            ast.BoolOp,
                            ast.Match,
                        ),
                    ):
                        complexity += 1

                if complexity > 10:

                    findings.append({

                        "agent": "Code Analysis",

                        "severity": "High",

                        "title": "High Cyclomatic Complexity",

                        "description":
                            f"Function '{node.name}' has complexity {complexity}.",

                        "line_number":
                            node.lineno,

                        "suggestion":
                            "Split the function into smaller functions."

                    })

        return findings