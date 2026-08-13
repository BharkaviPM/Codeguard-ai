from rag.retriever import get_vector_db


class RAGService:

    def __init__(self):
        self.db = get_vector_db()

    def retrieve(self, query):

        results = self.db.similarity_search_with_score(
            query,
            k=5
        )

        return results