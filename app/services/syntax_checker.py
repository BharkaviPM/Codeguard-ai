import ast


class SyntaxChecker:

    @staticmethod
    def detect_language(filename: str = "", code: str = ""):

        if filename.endswith(".py"):
            return "Python"

        if filename.endswith(".java"):
            return "Java"

        if "public class" in code:
            return "Java"

        return "Python"

    @staticmethod
    def validate_python(code: str):

        try:
            ast.parse(code)
            return True, "Valid Python Syntax"
        except SyntaxError as e:
            return False, str(e)

    @staticmethod
    def validate_java(code: str):

        if "class" not in code:
            return False, "No Java class found"

        if "{" not in code or "}" not in code:
            return False, "Missing braces"

        return True, "Valid Java Syntax"

    @staticmethod
    def validate(language: str, code: str):

        if language == "Python":
            return SyntaxChecker.validate_python(code)

        return SyntaxChecker.validate_java(code)