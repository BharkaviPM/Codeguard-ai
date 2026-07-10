from pathlib import Path

from radon.complexity import cc_visit
from radon.metrics import h_visit, mi_visit


class RadonService:

    def analyze(self, file_path: Path):

        try:

            source = file_path.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            # Cyclomatic Complexity
            complexity = cc_visit(source)

            complexity_data = []

            for item in complexity:

                complexity_data.append(
                    {
                        "name": item.name,
                        "type": item.__class__.__name__,
                        "complexity": item.complexity,
                        "line": item.lineno
                    }
                )

            # Maintainability Index
            maintainability = mi_visit(
                source,
                multi=True
            )

            # Halstead Metrics
            halstead = h_visit(source)

            return {

                "maintainability_index": round(
                    maintainability,
                    2
                ),

                "halstead": {

                    "vocabulary": halstead.total.vocabulary,

                    "length": halstead.total.length,

                    "volume": round(
                        halstead.total.volume,
                        2
                    ),

                    "difficulty": round(
                        halstead.total.difficulty,
                        2
                    ),

                    "effort": round(
                        halstead.total.effort,
                        2
                    )

                },

                "complexity": complexity_data

            }

        except Exception as ex:

            return {

                "error": str(ex)

            }