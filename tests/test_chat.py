from agents.chat_agent import ChatAgent

question = input("Ask: ")

answer = ChatAgent.ask(question)

print()
print(answer)