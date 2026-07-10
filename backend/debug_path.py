from pathlib import Path

base = Path("../knowledge_base").resolve()

print("Base:", base)
print("Exists:", base.exists())
print("Is Dir:", base.is_dir())

print("\nAll files:\n")

for f in base.rglob("*"):
    print(f)