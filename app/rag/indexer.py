import hashlib

from app.rag.loader import KnowledgeLoader
from app.rag.chunker import DocumentChunker
from app.rag.embedder import EmbeddingModel
from app.rag.vector_store import VectorStore


class KnowledgeIndexer:

    @staticmethod
    def build():

        print("Loading documents...")

        documents = KnowledgeLoader.load_documents()

        print(f"Loaded {len(documents)} pages")

        print("Splitting documents...")

        chunks = DocumentChunker.split(documents)

        print(f"Created {len(chunks)} chunks")

        model = EmbeddingModel.get_model()

        collection = VectorStore.get_collection()

        existing = collection.count()

        print(f"Existing Chunks : {existing}")

        ids = []
        embeddings = []
        texts = []
        metadatas = []

        for chunk in chunks:

            text = chunk.page_content.strip()

            if len(text) < 20:
                continue

            chunk_id = hashlib.md5(
                text.encode("utf-8")
            ).hexdigest()

            embedding = model.encode(text).tolist()

            ids.append(chunk_id)

            embeddings.append(embedding)

            texts.append(text)

            metadatas.append(
                chunk.metadata
            )

        collection.upsert(

            ids=ids,

            documents=texts,

            embeddings=embeddings,

            metadatas=metadatas

        )

        print("Knowledge Base Indexed Successfully")