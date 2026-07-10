import ast
from pathlib import Path


class MetricsService:

    def calculate(self, file_path: Path):

        text = file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        lines = text.splitlines()

        total = len(lines)

        blank = sum(
            1 for line in lines
            if not line.strip()
        )

        comments = sum(
            1
            for line in lines
            if line.strip().startswith("#")
        )

        code = total - blank - comments

        tree = ast.parse(text)

        functions = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.FunctionDef)
        ]

        classes = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.ClassDef)
        ]

        imports = [
            node
            for node in ast.walk(tree)
            if isinstance(
                node,
                (
                    ast.Import,
                    ast.ImportFrom
                )
            )
        ]

        lengths = []

        for func in functions:

            if hasattr(
                func,
                "end_lineno"
            ):

                lengths.append(
                    func.end_lineno - func.lineno + 1
                )

        average = (
            int(sum(lengths) / len(lengths))
            if lengths
            else 0
        )

        long_functions = len(
            [
                x
                for x in lengths
                if x > 30
            ]
        )

        return {

            "total_lines": total,

            "blank_lines": blank,

            "comment_lines": comments,

            "code_lines": code,

            "function_count": len(functions),

            "class_count": len(classes),

            "import_count": len(imports),

            "average_function_length": average,

            "long_functions": long_functions

        }