from pathlib import Path

ROOT = Path("../knowledge_base")

folders = [
    "OWASP",
    "CERT",
    "CWE",
    "Python",
    "Java"
]

for folder in folders:
    path = ROOT / folder
    path.mkdir(parents=True, exist_ok=True)
    print(f"Created: {path}")

print("\nKnowledge Base folder is ready.")