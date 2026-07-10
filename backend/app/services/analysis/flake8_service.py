from pathlib import Path
import subprocess


class Flake8Service:

    def analyze(self, file_path: Path):

        try:

            result = subprocess.run(

                [
                    "flake8",
                    str(file_path),
                    "--max-line-length=100"
                ],

                capture_output=True,

                text=True

            )

            issues = []

            if result.stdout:

                for line in result.stdout.splitlines():

                    parts = line.split(":", 3)

                    if len(parts) < 4:
                        continue

                    issues.append({

                        "line": int(parts[1]),

                        "column": int(parts[2]),

                        "message": parts[3].strip(),

                        "tool": "flake8",

                        "severity": "MEDIUM"

                    })

            return issues

        except Exception as ex:

            print(ex)

            return []