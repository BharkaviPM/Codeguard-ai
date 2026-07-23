from dataclasses import dataclass


@dataclass
class ASTMetrics:

    functions: int = 0

    classes: int = 0

    imports: int = 0

    loops: int = 0

    conditionals: int = 0

    try_blocks: int = 0

    lambda_functions: int = 0

    comprehensions: int = 0

    async_functions: int = 0