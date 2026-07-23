import ast

from app.analyzers.ast.metrics import ASTMetrics


class MetricsVisitor(ast.NodeVisitor):

    def __init__(self):

        self.metrics = ASTMetrics()

    def visit_FunctionDef(self, node):

        self.metrics.functions += 1

        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node):

        self.metrics.async_functions += 1

        self.generic_visit(node)

    def visit_ClassDef(self, node):

        self.metrics.classes += 1

        self.generic_visit(node)

    def visit_Import(self, node):

        self.metrics.imports += 1

    def visit_ImportFrom(self, node):

        self.metrics.imports += 1

    def visit_For(self, node):

        self.metrics.loops += 1

        self.generic_visit(node)

    def visit_While(self, node):

        self.metrics.loops += 1

        self.generic_visit(node)

    def visit_If(self, node):

        self.metrics.conditionals += 1

        self.generic_visit(node)

    def visit_Try(self, node):

        self.metrics.try_blocks += 1

        self.generic_visit(node)

    def visit_Lambda(self, node):

        self.metrics.lambda_functions += 1

    def visit_ListComp(self, node):

        self.metrics.comprehensions += 1