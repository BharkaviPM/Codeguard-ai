from rag.loader import PDFLoader
from rag.splitter import split_documents
from rag.embeddings import get_embeddings
from rag.vector_store import create_vector_store

loader = PDFLoader("knowledge_base/pdfs")

docs = loader.load_documents()

chunks = split_documents(docs)

embeddings = get_embeddings()

create_vector_store(
    chunks,
    embeddings
)

print("Knowledge Base Indexed Successfully")