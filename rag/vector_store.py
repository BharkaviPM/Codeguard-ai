from langchain_chroma import Chroma


def create_vector_store(chunks, embeddings):

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="vector_db"
    )

    return vectordb