from app.services.orchestrator import Orchestrator

code = """
import os

password="admin123"

user=input()

query="SELECT * FROM users WHERE id="+user

os.system(user)

eval(user)
"""

result = Orchestrator.analyze(

    language="Python",

    code=code,

    filename="sample.py"

)

print(result)