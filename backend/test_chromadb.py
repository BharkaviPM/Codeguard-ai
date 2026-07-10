from app.vectorstore.loader import DocumentLoader
from app.vectorstore.chunker import DocumentChunker
from app.vectorstore.embedding import EmbeddingGenerator
from app.vectorstore.chroma_manager import ChromaManager


loader = DocumentLoader("../knowledge_base")

documents = loader.load_documents()

print(f"Documents : {len(documents)}")

chunker = DocumentChunker()

chunks = chunker.chunk_documents(documents)

print(f"Chunks : {len(chunks)}")

embedder = EmbeddingGenerator()

embedded = embedder.generate_embeddings(chunks)

print("Embeddings Generated")

db = ChromaManager()

db.reset()

db.add_documents(embedded)

print()

print("Total Stored Chunks")

print(db.count())