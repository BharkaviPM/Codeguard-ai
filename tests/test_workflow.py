from workflows.review_workflow import ReviewWorkflow

code = """
user = input()

query = "SELECT * FROM users WHERE name='" + user + "'"

cursor.execute(query)
"""

workflow = ReviewWorkflow()

result = workflow.run(code)

print(result)