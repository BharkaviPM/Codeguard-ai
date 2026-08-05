import ast

from app.analyzers.complexity import ComplexityAnalyzer
from app.analyzers.magic_number import MagicNumberAnalyzer
from app.analyzers.naming import NamingAnalyzer


class PythonAnalyzer:

    @staticmethod
    def analyze(code: str):

        findings = []

        # -----------------------------
        # Parse Python Code
        # -----------------------------
        try:
            tree = ast.parse(code)

        except SyntaxError as e:

            findings.append({

                "agent": "Code Analysis",

                "severity": "Critical",

                "title": "Syntax Error",

                "description": str(e),

                "line_number": e.lineno or 0,

                "suggestion":
                    "Fix the syntax error before analysis."
            })

            return findings

        # -----------------------------
        # Long Functions
        # -----------------------------
        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                end = getattr(node, "end_lineno", node.lineno)

                length = end - node.lineno + 1

                if length > 40:

                    findings.append({

                        "agent": "Code Analysis",

                        "severity": "Medium",

                        "title": "Long Function",

                        "description":
                            f"'{node.name}' contains {length} lines.",

                        "line_number":
                            node.lineno,

                        "suggestion":
                            "Split the function into smaller functions."
                    })

        # -----------------------------
        # Too Many Parameters
        # -----------------------------
        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                arg_count = len(node.args.args)

                if arg_count > 5:

                    findings.append({

                        "agent": "Code Analysis",

                        "severity": "Medium",

                        "title": "Too Many Parameters",

                        "description":
                            f"'{node.name}' has {arg_count} parameters.",

                        "line_number":
                            node.lineno,

                        "suggestion":
                            "Reduce parameters or use a class/dataclass."
                    })

        # -----------------------------
        # Missing Docstrings
        # -----------------------------
        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                if ast.get_docstring(node) is None:

                    findings.append({

                        "agent": "Code Analysis",

                        "severity": "Low",

                        "title": "Missing Docstring",

                        "description":
                            f"'{node.name}' has no documentation.",

                        "line_number":
                            node.lineno,

                        "suggestion":
                            "Add a docstring."
                    })

        # -----------------------------
        # Deep Nesting
        # -----------------------------
        def check_depth(node, depth=0):

            if depth > 4:

                findings.append({

                    "agent": "Code Analysis",

                    "severity": "Medium",

                    "title": "Deep Nesting",

                    "description":
                        "Nested blocks exceed recommended depth.",

                    "line_number":
                        getattr(node, "lineno", 0),

                    "suggestion":
                        "Refactor nested logic into helper functions."
                })

            for child in ast.iter_child_nodes(node):

                if isinstance(
                    child,
                    (
                        ast.If,
                        ast.For,
                        ast.While,
                        ast.Try,
                        ast.With,
                        ast.Match,
                    ),
                ):
                    check_depth(child, depth + 1)

                else:
                    check_depth(child, depth)

        check_depth(tree)

        # -----------------------------
        # Duplicate Imports
        # -----------------------------
        imports = []

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for alias in node.names:

                    if alias.name in imports:

                        findings.append({

                            "agent": "Code Analysis",

                            "severity": "Low",

                            "title": "Duplicate Import",

                            "description":
                                f"'{alias.name}' imported multiple times.",

                            "line_number":
                                node.lineno,

                            "suggestion":
                                "Remove duplicate import."
                        })

                    imports.append(alias.name)

        # -----------------------------
        # Empty Functions
        # -----------------------------
        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                body = node.body

                if len(body) == 1:

                    stmt = body[0]

                    if isinstance(stmt, ast.Pass):

                        findings.append({

                            "agent": "Code Analysis",

                            "severity": "Low",

                            "title": "Empty Function",

                            "description":
                                f"'{node.name}' contains only pass.",

                            "line_number":
                                node.lineno,

                            "suggestion":
                                "Implement or remove the function."
                        })

        # -----------------------------
        # External Analyzers
        # -----------------------------
        findings.extend(

            ComplexityAnalyzer.analyze(tree)

        )

        findings.extend(

            MagicNumberAnalyzer.analyze(tree)

        )

        findings.extend(

            NamingAnalyzer.analyze(tree)

        )

        return findings