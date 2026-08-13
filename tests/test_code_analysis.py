from agents.code_analysis_agent import CodeAnalysisAgent

sample_code = """
def calculate(a,b,c,d,e,f,g,h):

    if a:
        if b:
            if c:
                if d:
                    if e:
                        if f:
                            if g:
                                if h:
                                    return True

    return False
"""

agent = CodeAnalysisAgent()

findings = agent.analyze_python(
    sample_code
)

for finding in findings:
    print(finding)