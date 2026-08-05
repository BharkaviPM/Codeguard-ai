from app.services.rag_service import RAGService

#question = "What is SQL Injection?"
#question="Explain XSS Prevention"
question="Secure Java Coding Guidelines"
answer = RAGService.ask(question)

print(answer)