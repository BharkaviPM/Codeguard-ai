from app.vectorstore.loader import DocumentLoader
from app.vectorstore.chunker import DocumentChunker


loader = DocumentLoader("../knowledge_base")

documents = loader.load_documents()

print(f"Loaded Documents : {len(documents)}")

chunker = DocumentChunker()

chunks = chunker.chunk_documents(documents)

print(f"Generated Chunks : {len(chunks)}")

print("=" * 80)

first = chunks[0]

print(first["metadata"])

print()

print(first["text"][:500])