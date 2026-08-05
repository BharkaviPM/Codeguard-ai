from app.rag.retriever import Retriever
from app.services.groq_service import GroqService


class RAGService:

    @staticmethod
    def ask(question):

        results = Retriever.search(question)

        documents = results["documents"][0]

        context = "\n\n".join(documents)

        prompt = f"""
You are CodeGuard AI.

Answer ONLY using the secure coding knowledge provided below.

If the answer is not found in the context,
say:

"I couldn't find this in the knowledge base."

========================

Context

{context}

========================

Question

{question}

========================

Answer
"""

        return GroqService.chat(prompt)