# utils/code_metrics.py

import re


class CodeMetrics:

    @staticmethod
    def calculate(code):

        lines = len(
            code.splitlines()
        )

        functions = len(
            re.findall(
                r"def\s+\w+",
                code
            )
        )

        classes = len(
            re.findall(
                r"class\s+\w+",
                code
            )
        )

        return {
            "lines": lines,
            "functions": functions,
            "classes": classes
        }