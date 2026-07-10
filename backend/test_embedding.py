from app.vectorstore.loader import DocumentLoader
from app.vectorstore.chunker import DocumentChunker
from app.vectorstore.embedding import EmbeddingGenerator


loader = DocumentLoader("../knowledge_base")

documents = loader.load_documents()

chunker = DocumentChunker()

chunks = chunker.chunk_documents(documents)

embedder = EmbeddingGenerator()

embedded = embedder.generate_embeddings(chunks[:1])

print("=" * 80)

print("Embedding Dimension")

print(len(embedded[0]["embedding"]))

print("=" * 80)

print(embedded[0]["metadata"])