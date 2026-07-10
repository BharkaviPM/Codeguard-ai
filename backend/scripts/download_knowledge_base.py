from pathlib import Path
import requests

BASE = Path("../knowledge_base")

FOLDERS = [
    "OWASP",
    "CERT",
    "CWE",
    "Python",
    "Java"
]

for folder in FOLDERS:
    (BASE / folder).mkdir(parents=True, exist_ok=True)

DOWNLOADS = [
    {
        "folder": "Python",
        "name": "Python_Security_Warnings.pdf",
        "url": "https://docs.python.org/3/_downloads/python-docs-pdf-a4.zip"
    }
]

for item in DOWNLOADS:

    destination = BASE / item["folder"] / item["name"]

    if destination.exists():
        print(f"✓ {destination.name} already exists")
        continue

    try:

        print(f"Downloading {item['name']}")

        response = requests.get(item["url"], timeout=60)

        response.raise_for_status()

        with open(destination, "wb") as f:
            f.write(response.content)

        print("Done")

    except Exception as ex:

        print(f"Failed: {item['name']}")

        print(ex)

print("\nKnowledge base folders are ready.")
print("Some documents require manual download.")