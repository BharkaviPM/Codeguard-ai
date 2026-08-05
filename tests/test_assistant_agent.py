from app.agents.assistant_agent import AssistantAgent

question = "How do I prevent SQL Injection?"

result = AssistantAgent.ask(question)

print(result)