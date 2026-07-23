from __future__ import annotations

import ast
import time
from pathlib import Path

from app.agents.analysis.models import AnalysisResult
from app.analyzers.ast.smells import SmellVisitor
from app.analyzers.ast.visitor import MetricsVisitor
from app.analyzers.base import BaseAnalyzer


class ASTAnalyzer(BaseAnalyzer):
    """
    AST-based code analyzer.

    Collects:

    • Classes
    • Functions
    • Imports
    • Loops
    • Branches
    • Code smells

    Returns AnalysisResult.
    """

    name = "AST"

    supported_languages = ["Python"]

    def analyze(
        self,
        project_path: str,
    ) -> AnalysisResult:

        start = time.perf_counter()

        result = AnalysisResult(
            analyzer=self.name,
            findings=[],
            metrics={},
            execution_time=0.0,
        )

        project = Path(project_path)

        python_files = list(project.rglob("*.py"))

        summary = {
            "files_scanned": 0,
            "functions": 0,
            "classes": 0,
            "imports": 0,
            "branches": 0,
            "loops": 0,
            "syntax_errors": 0,
        }

        for file in python_files:

            try:

                source = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

                tree = ast.parse(
                    source,
                    filename=str(file),
                )

            except SyntaxError:

                summary["syntax_errors"] += 1

                continue

            except Exception:

                continue

            metric_visitor = MetricsVisitor()

            metric_visitor.visit(tree)

            smell_visitor = SmellVisitor()

            smell_visitor.visit(tree)

            metrics = vars(
                metric_visitor.metrics
            )

            result.metrics[str(file)] = metrics

            summary["files_scanned"] += 1

            summary["functions"] += metrics.get(
                "functions",
                0,
            )

            summary["classes"] += metrics.get(
                "classes",
                0,
            )

            summary["imports"] += metrics.get(
                "imports",
                0,
            )

            summary["branches"] += metrics.get(
                "branches",
                0,
            )

            summary["loops"] += metrics.get(
                "loops",
                0,
            )

            for finding in smell_visitor.findings:

                finding.file = str(file)

                result.findings.append(
                    finding
                )

        result.metrics["summary"] = summary

        result.execution_time = round(
            time.perf_counter() - start,
            3,
        )

        return result