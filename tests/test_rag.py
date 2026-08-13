from rag.retriever import get_vector_db
from rag.domain_guard import is_security_query


class RAGService:

    THRESHOLD = 1.2

    def __init__(self):
        self.db = get_vector_db()

    def retrieve(self, query):

        results = self.db.similarity_search_with_score(
            query,
            k=5
        )

        return [
            (doc, score)
            for doc, score in results
            if score <= self.THRESHOLD
        ]

    def answer(self, query):

        if not is_security_query(query):
            return {
                "success": False,
                "message": (
                    "This assistant only answers questions "
                    "related to OWASP, CWE, CERT, secure coding, "
                    "security vulnerabilities, and code quality."
                )
            }

        docs = self.retrieve(query)

        if not docs:
            return {
                "success": False,
                "message": (
                    "No relevant information found in the "
                    "knowledge base."
                )
            }

        return {
            "success": True,
            "documents": docs
        }