import ast
from pathlib import Path


class ASTAnalyzer:

    def analyze(self, file_path: Path):

        source = file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

        tree = ast.parse(source)

        imports = []

        classes = []

        functions = []

        async_functions = []

        globals_ = []

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for alias in node.names:

                    imports.append(alias.name)

            elif isinstance(node, ast.ImportFrom):

                module = node.module or ""

                imports.append(module)

            elif isinstance(node, ast.ClassDef):

                classes.append(node.name)

            elif isinstance(node, ast.FunctionDef):

                functions.append(node.name)

            elif isinstance(node, ast.AsyncFunctionDef):

                async_functions.append(node.name)

            elif isinstance(node, ast.Assign):

                for target in node.targets:

                    if isinstance(target, ast.Name):

                        globals_.append(target.id)

        return {

            "imports": imports,

            "classes": classes,

            "functions": functions,

            "async_functions": async_functions,

            "globals": globals_,

            "num_imports": len(imports),

            "num_classes": len(classes),

            "num_functions": len(functions),

            "num_async_functions": len(async_functions),

            "num_globals": len(globals_)

        }