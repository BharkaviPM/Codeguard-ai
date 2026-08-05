from app.agents.summary_agent import SummaryAgent

findings = [

    {
        "title": "SQL Injection",
        "severity": "Critical",
        "description": "Dynamic SQL",
        "suggestion": "Parameterized Query"
    },

    {
        "title": "Hardcoded Secret",
        "severity": "High",
        "description": "Password",
        "suggestion": "Environment Variable"
    },

    {
        "title": "Missing Docstring",
        "severity": "Low",
        "description": "No documentation",
        "suggestion": "Add Docstring"
    }

]

remediation = """
SQL Injection fixed.

Hardcoded Secret removed.

Added documentation.
"""

result = SummaryAgent.generate_summary(

    "Python",

    "print('Hello')",

    findings,

    remediation

)

print(result)