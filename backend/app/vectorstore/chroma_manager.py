from chromadb import PersistentClient


class ChromaManager:
    """
    Handles ChromaDB operations.
    """

    def __init__(
        self,
        db_path: str = "../vector_db",
        collection_name: str = "secure_coding"
    ):

        self.client = PersistentClient(path=db_path)

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add_documents(self, embedded_chunks):

        ids = []
        documents = []
        embeddings = []
        metadatas = []

        for index, chunk in enumerate(embedded_chunks):

            ids.append(
                f"{chunk['metadata']['filename']}_{chunk['metadata']['chunk_id']}"
            )

            documents.append(chunk["text"])

            embeddings.append(chunk["embedding"])

            metadatas.append(chunk["metadata"])

        self.collection.add(

            ids=ids,

            documents=documents,

            embeddings=embeddings,

            metadatas=metadatas

        )

    def count(self):

        return self.collection.count()

    def get_collection(self):

        return self.collection

    def reset(self):

        self.client.delete_collection(
            self.collection.name
        )

        self.collection = self.client.get_or_create_collection(
            name=self.collection.name
        )