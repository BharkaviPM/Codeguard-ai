# tests/test_full_review.py

from workflows.review_workflow import ReviewWorkflow

code = """
import sqlite3

def login(username,password):

    conn = sqlite3.connect("users.db")

    query = f"SELECT * FROM users WHERE username='{username}'"

    return conn.execute(query).fetchone()
"""

workflow = ReviewWorkflow()

result = workflow.run(code)

print(result)