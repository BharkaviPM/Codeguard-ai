from ollama import Client


class EmbeddingGenerator:
    """
    Generates embeddings using Ollama.
    """

    def __init__(self):

        self.client = Client(
            host="http://localhost:11434"
        )

        self.model = "nomic-embed-text"

    def generate_embedding(
        self,
        text: str
    ):

        response = self.client.embeddings(

            model=self.model,

            prompt=text

        )

        return response["embedding"]

    def generate_embeddings(
        self,
        chunks
    ):

        embedded_chunks = []

        for chunk in chunks:

            embedding = self.generate_embedding(
                chunk["text"]
            )

            embedded_chunks.append({

                "text": chunk["text"],

                "embedding": embedding,

                "metadata": chunk["metadata"]

            })

        return embedded_chunks