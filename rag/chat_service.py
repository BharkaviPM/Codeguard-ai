# rag/chat_service.py

from rag.rag_service import RAGService
from services.groq_service import GroqService


class ChatService:
    """
    Grounded secure-coding chat service.

    Flow:

        User Question
              ↓
        ChromaDB Retrieval
              ↓
        Relevance Check
              ↓
        Groq LLM
              ↓
        Grounded Answer

    The LLM is only called when relevant knowledge-base
    documents are retrieved.
    """

    # Lower Chroma distance = better match.
    #
    # This is intentionally conservative.
    # It should be tuned using your actual knowledge base.
    RELEVANCE_THRESHOLD = 1.0

    def __init__(self):
        self.rag = RAGService()

    def ask(self, question: str) -> str:

        if not question or not question.strip():
            return "Please enter a secure-coding question."

        question = question.strip()

        try:
            results = self.rag.retrieve(question)

        except Exception as exc:
            return (
                "Unable to search the secure-coding knowledge base. "
                f"Error: {exc}"
            )

        if not results:
            return (
                "This question is outside the secure coding "
                "knowledge base."
            )

        # results are:
        #
        # [
        #     (Document, score),
        #     (Document, score),
        #     ...
        # ]

        relevant_documents = []

        for document, score in results:

            if score <= self.RELEVANCE_THRESHOLD:
                relevant_documents.append(
                    (document, score)
                )

        # No sufficiently relevant document.
        if not relevant_documents:
            return (
                "This question is outside the secure coding "
                "knowledge base."
            )

        # Build grounded context.
        context_parts = []

        for document, score in relevant_documents:

            content = document.page_content

            if content and content.strip():

                context_parts.append(
                    content.strip()
                )

        if not context_parts:
            return (
                "I could not find usable information for this "
                "question in the secure coding knowledge base."
            )

        context = "\n\n---\n\n".join(context_parts)

        prompt = f"""
You are CodeGuard AI, a secure-coding assistant.

You MUST answer ONLY using the provided knowledge-base context.

IMPORTANT RULES:

1. Use only the supplied context.
2. Do not use outside knowledge.
3. Do not invent facts.
4. Do not answer unrelated questions.
5. If the context does not contain enough information to answer
   the question, say:

   "This question is outside the secure coding knowledge base."

6. Keep the answer focused on secure coding.
7. When appropriate, mention the relevant security practice,
   vulnerability, or mitigation described in the context.
8. Do not pretend that information exists in the knowledge base
   when it does not.

KNOWLEDGE BASE CONTEXT:

{context}

USER QUESTION:

{question}

ANSWER:
"""

        try:

            answer = GroqService.chat(prompt)

        except Exception as exc:

            return (
                "Unable to generate the answer using Groq. "
                f"Error: {exc}"
            )

        if not answer or not answer.strip():

            return (
                "The knowledge base contained relevant information, "
                "but no answer could be generated."
            )

        return answer.strip()