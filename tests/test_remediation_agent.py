from app.agents.remediation_agent import RemediationAgent

code = """
password="admin123"

user=input()

query="SELECT * FROM users WHERE id="+user

eval(user)
"""

findings = [

    {

        "title":"SQL Injection",

        "severity":"Critical",

        "description":"Dynamic SQL",

        "suggestion":"Parameterized Query"

    },

    {

        "title":"Hardcoded Secret",

        "severity":"High",

        "description":"Password in code",

        "suggestion":"Environment Variable"

    }

]

result = RemediationAgent.generate_fix(

    "Python",

    code,

    findings

)

print(result)