from app.rag.embedder import EmbeddingModel
from app.rag.vector_store import VectorStore


class Retriever:

    @staticmethod
    def search(question):

        model = EmbeddingModel.get_model()

        embedding = model.encode(question).tolist()

        collection = VectorStore.get_collection()

        results = collection.query(

            query_embeddings=[embedding],

            n_results=5

        )

        return results