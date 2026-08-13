from services.groq_service import GroqService

llm = GroqService()

response = llm.invoke(
    "Explain SQL Injection in one sentence."
)

print(response)