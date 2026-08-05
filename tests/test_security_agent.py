from app.agents.security_agent import SecurityAgent

code = """
import os

password="admin123"

user=input()

query="SELECT * FROM users WHERE id="+user

os.system(user)

eval(user)
"""

result = SecurityAgent.analyze(

    "Python",

    code

)

print(result)