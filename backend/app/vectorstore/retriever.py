from app.vectorstore.embedding import EmbeddingGenerator
from app.vectorstore.chroma_manager import ChromaManager


class Retriever:

    def __init__(self):

        self.embedder = EmbeddingGenerator()

        self.db = ChromaManager()

    def search(
        self,
        query: str,
        top_k: int = 5
    ):

        query_embedding = self.embedder.generate_embedding(
            query
        )

        results = self.db.collection.query(

            query_embeddings=[query_embedding],

            n_results=top_k

        )

        documents = []

        if not results["ids"]:

            return documents

        for i in range(len(results["ids"][0])):

            documents.append({

                "id": results["ids"][0][i],

                "text": results["documents"][0][i],

                "metadata": results["metadatas"][0][i],

                "distance": results["distances"][0][i]

            })

        return documents