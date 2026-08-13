from agents.security_agent import SecurityAgent

vulnerable_code = """
import sqlite3

username = input()

query = f"SELECT * FROM users WHERE name='{username}'"

conn = sqlite3.connect("db.sqlite")

cursor = conn.cursor()

cursor.execute(query)
"""

agent = SecurityAgent()

findings = agent.analyze_python(
    vulnerable_code
)

for finding in findings:

    print()
    print("TOOL:", finding.tool)
    print("SEVERITY:", finding.severity)
    print("TITLE:", finding.title)
    print("LINE:", finding.line_number)
    print("DESC:", finding.description)