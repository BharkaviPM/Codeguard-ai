from rag.chat_service import ChatService


chat = ChatService()


questions = [
    "How can SQL Injection be prevented?",
    "What is the price of iPhone 17?"
]


for question in questions:

    print("\n" + "=" * 60)
    print("QUESTION:", question)
    print("=" * 60)

    answer = chat.ask(question)

    print(answer)