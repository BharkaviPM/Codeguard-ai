from rag.rag_service import RAGService
from services.groq_service import GroqService


class ChatAgent:

    @staticmethod
    def ask(question: str):

        rag = RAGService()

        docs = rag.retrieve(question)

        if not docs:
            return (
                "No relevant secure coding information "
                "found in the knowledge base."
            )

        context = "\n\n".join(
            doc.page_content
            for doc, score in docs
        )

        prompt = f"""
You are an OWASP Secure Coding Assistant.

IMPORTANT RULES:

1. Answer ONLY using the provided context.
2. If the answer is not present in the context, say:
   "This question is outside the secure coding knowledge base."
3. Do not make up information.

Context:

{context}

Question:

{question}

Answer:
"""

        return GroqService.chat(prompt)