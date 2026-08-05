from app.agents.code_agent import CodeAnalysisAgent

code = """
def add(a,b):
    return a+b
"""

result = CodeAnalysisAgent.analyze(

    "Python",

    code

)

print(result)