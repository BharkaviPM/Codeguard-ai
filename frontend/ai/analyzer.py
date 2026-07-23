import ast
import os
import re
import zipfile
import tempfile

from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Dict, Any

import ollama

# =====================================================
# Models
# =====================================================

@dataclass
class SecurityIssue:
    severity: str
    issue: str
    file: str
    line: int
    recommendation: str


@dataclass
class Finding:
    severity: str
    issue: str
    file: str
    line: int


@dataclass
class ComplexityMetric:
    function: str
    complexity: int


@dataclass
class ProjectMetrics:
    total_files: int
    total_lines: int
    total_functions: int
    total_classes: int
    average_complexity: float


# =====================================================
# Analyzer
# =====================================================

class CodeAnalyzer:

    def __init__(self):
        print("Initializing Code Analyzer...")
        self.security = []
        self.findings = []
        self.complexity = []

        self.total_files = 0
        self.total_lines = 0
        self.total_functions = 0
        self.total_classes = 0

    # =================================================

    def analyze_project(
        self,
        project_path: str,
    ) -> Dict[str, Any]:

        path = Path(project_path)

        if not path.exists():

            raise FileNotFoundError(project_path)

        files = []

        if path.suffix.lower() == ".zip":

            files = self.extract_zip(path)

        else:

            files.append(path)

        self.total_files = len(files)

        for file in files:

            self.analyze_file(file)

        metrics = ProjectMetrics(

            total_files=self.total_files,

            total_lines=self.total_lines,

            total_functions=self.total_functions,

            total_classes=self.total_classes,

            average_complexity=self.average_complexity(),

        )

        summary = self.generate_summary(metrics)

        return {

            "summary": summary,

            "metrics": [
                asdict(metrics)
            ],

            "complexity": [
                asdict(x)
                for x in self.complexity
            ],

            "security": [
                asdict(x)
                for x in self.security
            ],

            "findings": [
                asdict(x)
                for x in self.findings
            ],

            "ai_summary": summary["ai_summary"],
        }

    # =================================================

    def extract_zip(
        self,
        zip_path: Path,
    ) -> List[Path]:

        temp_dir = tempfile.mkdtemp()

        with zipfile.ZipFile(zip_path) as archive:

            archive.extractall(temp_dir)

        files = []

        for root, _, filenames in os.walk(temp_dir):

            for file in filenames:

                if file.endswith(".py") or file.endswith(".java"):

                    files.append(

                        Path(root) / file

                    )

        return files

    # =================================================

    def analyze_file(
        self,
        file_path: Path,
    ):

        if file_path.suffix == ".py":

            self.analyze_python(file_path)

        elif file_path.suffix == ".java":

            self.analyze_java(file_path)

    # =================================================

    def average_complexity(self):

        if not self.complexity:

            return 0

        return round(

            sum(
                x.complexity
                for x in self.complexity
            )

            / len(self.complexity),

            2,

        )

        # =====================================================
    # Python Analysis
    # =====================================================

    def analyze_python(
        self,
        file_path: Path,
    ):

        try:

            code = file_path.read_text(
                encoding="utf-8",
                errors="ignore",
            )

        except Exception:

            return

        self.total_lines += len(
            code.splitlines()
        )

        try:

            tree = ast.parse(code)

        except Exception:

            self.findings.append(

                Finding(
                    severity="HIGH",
                    issue="Python syntax error",
                    file=file_path.name,
                    line=1,
                )

            )

            return

        for node in ast.walk(tree):

            if isinstance(node, ast.FunctionDef):

                self.total_functions += 1

                complexity = self.calculate_complexity(
                    node
                )

                self.complexity.append(

                    ComplexityMetric(
                        function=node.name,
                        complexity=complexity,
                    )

                )

                if complexity > 15:

                    self.findings.append(

                        Finding(
                            severity="HIGH",
                            issue="Very High Cyclomatic Complexity",
                            file=file_path.name,
                            line=node.lineno,
                        )

                    )

                elif complexity > 8:

                    self.findings.append(

                        Finding(
                            severity="MEDIUM",
                            issue="Complex Function",
                            file=file_path.name,
                            line=node.lineno,
                        )

                    )

            elif isinstance(node, ast.ClassDef):

                self.total_classes += 1

        self.security_scan_python(

            tree,

            code,

            file_path.name,

        )

        self.code_smell_scan(

            code,

            file_path.name,

        )

    # =====================================================
    # Java Analysis
    # =====================================================

    def analyze_java(
        self,
        file_path: Path,
    ):

        try:

            code = file_path.read_text(
                encoding="utf-8",
                errors="ignore",
            )

        except Exception:

            return

        self.total_lines += len(
            code.splitlines()
        )

        self.total_classes += len(

            re.findall(
                r"\bclass\b",
                code,
            )

        )

        functions = re.findall(

            r"(public|private|protected).*?\(",
            code,

        )

        self.total_functions += len(
            functions
        )

        for match in re.finditer(

            r"(public|private|protected).*?\(",
            code,

        ):

            self.complexity.append(

                ComplexityMetric(

                    function="Java Method",

                    complexity=2,

                )

            )

        self.code_smell_scan(

            code,

            file_path.name,

        )

    # =====================================================
    # Cyclomatic Complexity
    # =====================================================

    def calculate_complexity(
        self,
        node,
    ):

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
                    ast.With,
                    ast.ExceptHandler,
                    ast.Match,
                ),

            ):

                complexity += 1

        return complexity

    # =====================================================
    # Security Scan
    # =====================================================

    def security_scan_python(

        self,

        tree,

        code,

        filename,

    ):

        for node in ast.walk(tree):

            if isinstance(node, ast.Call):

                if getattr(node.func, "id", "") == "eval":

                    self.security.append(

                        SecurityIssue(

                            severity="CRITICAL",

                            issue="Use of eval()",

                            file=filename,

                            line=node.lineno,

                            recommendation="Avoid eval().",

                        )

                    )

                if getattr(node.func, "id", "") == "exec":

                    self.security.append(

                        SecurityIssue(

                            severity="HIGH",

                            issue="Use of exec()",

                            file=filename,

                            line=node.lineno,

                            recommendation="Avoid exec().",

                        )

                    )

        patterns = [

            r"password\s*=",

            r"passwd\s*=",

            r"secret\s*=",

            r"token\s*=",

            r"api_key\s*=",

        ]

        for pattern in patterns:

            for match in re.finditer(

                pattern,

                code,

                flags=re.IGNORECASE,

            ):

                line = code.count(

                    "\n",

                    0,

                    match.start(),

                ) + 1

                self.security.append(

                    SecurityIssue(

                        severity="MEDIUM",

                        issue="Possible hardcoded credential",

                        file=filename,

                        line=line,

                        recommendation="Move secrets into environment variables.",

                    )

                )

        if "shell=True" in code:

            self.security.append(

                SecurityIssue(

                    severity="HIGH",

                    issue="shell=True detected",

                    file=filename,

                    line=1,

                    recommendation="Avoid shell=True in subprocess.",

                )

            )

    # =====================================================
    # Code Smell Detection
    # =====================================================

    def code_smell_scan(

        self,

        code,

        filename,

    ):

        lines = code.splitlines()

        if len(lines) > 500:

            self.findings.append(

                Finding(

                    severity="LOW",

                    issue="Large source file",

                    file=filename,

                    line=1,

                )

            )

        long_lines = 0

        for i, line in enumerate(lines):

            if len(line) > 120:

                long_lines += 1

                self.findings.append(

                    Finding(

                        severity="LOW",

                        issue="Very long line",

                        file=filename,

                        line=i + 1,

                    )

                )

        if long_lines > 20:

            self.findings.append(

                Finding(

                    severity="MEDIUM",

                    issue="Too many long lines",

                    file=filename,

                    line=1,

                )

            )

                # =====================================================
    # Health Score
    # =====================================================

    def calculate_health_score(self):

        score = 100

        score -= len(self.security) * 8

        score -= len(self.findings) * 2

        avg_complexity = self.average_complexity()

        if avg_complexity > 15:

            score -= 20

        elif avg_complexity > 10:

            score -= 10

        elif avg_complexity > 5:

            score -= 5

        return max(score, 0)

    # =====================================================
    # Maintainability
    # =====================================================

    def maintainability_score(self):

        score = 100

        score -= len(self.findings)

        score -= int(self.average_complexity() * 2)

        if self.total_lines > 1000:

            score -= 10

        return max(score, 0)

    # =====================================================
    # Severity Counts
    # =====================================================

    def severity_counts(self):

        critical = 0
        high = 0
        medium = 0
        low = 0

        for issue in self.security:

            if issue.severity == "CRITICAL":

                critical += 1

            elif issue.severity == "HIGH":

                high += 1

            elif issue.severity == "MEDIUM":

                medium += 1

            else:

                low += 1

        for finding in self.findings:

            if finding.severity == "HIGH":

                high += 1

            elif finding.severity == "MEDIUM":

                medium += 1

            else:

                low += 1

        return {

            "critical": critical,

            "high": high,

            "medium": medium,

            "low": low,

        }

     # =====================================================
    # AI Summary
    # =====================================================

    def generate_ai_summary(self, metrics: ProjectMetrics) -> str:

        prompt = f"""
You are a senior software security engineer.

Analyze the following static code analysis report.

Project Metrics:
- Files: {metrics.total_files}
- Lines: {metrics.total_lines}
- Functions: {metrics.total_functions}
- Classes: {metrics.total_classes}
- Average Complexity: {metrics.average_complexity}

Security Issues Found: {len(self.security)}
Code Quality Findings: {len(self.findings)}

Critical Security Issues:
{[s.issue for s in self.security if s.severity == "CRITICAL"]}

High Severity Issues:
{[s.issue for s in self.security if s.severity == "HIGH"]}

Generate a concise report with the following sections:

1. Overall Project Health
2. Security Assessment
3. Code Quality Assessment
4. Maintainability
5. Top Recommendations

Limit the response to about 200 words.
"""

        try:

            response = ollama.chat(

                model="llama3:latest",

                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],

            )

            return response["message"]["content"]

        except Exception as e:

            return (
                "Unable to generate AI summary using Ollama.\n"
                f"Reason: {str(e)}"
            )


    # =====================================================
    # Final Summary
    # =====================================================

    def generate_summary(
        self,
        metrics: ProjectMetrics,
    ):

        severity = self.severity_counts()

        health = self.calculate_health_score()

        maintainability = self.maintainability_score()

        return {

            "health_score": health,

            "maintainability": maintainability,

            "security": len(self.security),

            "quality": len(self.findings),

            "critical": severity["critical"],

            "high": severity["high"],

            "medium": severity["medium"],

            "low": severity["low"],

            "ai_summary": self.generate_ai_summary(
                metrics
            ),

        }

    # =====================================================
# Public API
# =====================================================

def analyze_project(project_path: str):

    analyzer = CodeAnalyzer()

    return analyzer.analyze_project(project_path)


# =====================================================
# Standalone Test
# =====================================================

if __name__ == "__main__":

    sample = input("Enter project path: ")

    result = analyze_project(sample)

    print("\n========== SUMMARY ==========\n")

    print(result["summary"])

    print("\n========== METRICS ==========\n")

    print(result["metrics"])

    print("\n========== SECURITY ==========\n")

    print(result["security"])

    print("\n========== FINDINGS ==========\n")

    print(result["findings"])

    print("\n========== COMPLEXITY ==========\n")

    print(result["complexity"])

    print("\n========== AI SUMMARY ==========\n")

    print(result["ai_summary"])