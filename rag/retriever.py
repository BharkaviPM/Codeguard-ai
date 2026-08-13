from langchain_chroma import Chroma
from rag.embeddings import get_embeddings


def get_vector_db():

    return Chroma(
        persist_directory="vector_db",
        embedding_function=get_embeddings()
    )