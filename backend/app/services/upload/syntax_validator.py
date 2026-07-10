import ast


class SyntaxValidator:

    def validate(
        self,
        language: str,
        source_code: str
    ):

        if language == "Python":
            return self.validate_python(source_code)

        if language == "Java":
            return self.validate_java(source_code)

        return {

            "valid": False,

            "language": language,

            "error": "Unsupported language."

        }

    def validate_python(
        self,
        source_code: str
    ):

        try:

            ast.parse(source_code)

            return {

                "valid": True,

                "language": "Python",

                "error": None

            }

        except SyntaxError as ex:

            return {

                "valid": False,

                "language": "Python",

                "error": f"Line {ex.lineno}: {ex.msg}"

            }

    def validate_java(
        self,
        source_code: str
    ):

        errors = []

        # ---------- Balanced Braces ----------

        if source_code.count("{") != source_code.count("}"):

            errors.append(
                "Unbalanced braces."
            )

        # ---------- Class ----------

        if "class " not in source_code:

            errors.append(
                "Missing class declaration."
            )

        # ---------- Main Method ----------

        if "main(" not in source_code:

            errors.append(
                "Main method not found."
            )

        if errors:

            return {

                "valid": False,

                "language": "Java",

                "error": "; ".join(errors)

            }

        return {

            "valid": True,

            "language": "Java",

            "error": None

        }