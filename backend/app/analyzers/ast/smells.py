import ast

from app.agents.analysis.models import Finding
from app.agents.analysis.models import Severity


class SmellVisitor(ast.NodeVisitor):

    def __init__(self):

        self.findings = []

    def visit_FunctionDef(self, node):

        # Too many parameters

        if len(node.args.args) > 5:

            self.findings.append(

                Finding(

                    tool="AST",

                    category="Code Smell",

                    title="Too Many Parameters",

                    description=f"{node.name} has {len(node.args.args)} parameters.",

                    severity=Severity.MEDIUM,

                    file="",

                    line=node.lineno,

                    recommendation="Reduce parameter count."

                )

            )

        # Long function

        if hasattr(node, "end_lineno"):

            lines = node.end_lineno - node.lineno

            if lines > 50:

                self.findings.append(

                    Finding(

                        tool="AST",

                        category="Code Smell",

                        title="Long Function",

                        description=f"{node.name} contains {lines} lines.",

                        severity=Severity.MEDIUM,

                        file="",

                        line=node.lineno,

                        recommendation="Split into smaller functions."

                    )

                )

        self.generic_visit(node)