from ollama import Client

from app.vectorstore.retriever import Retriever


class RAGService:

    def __init__(self):

        self.retriever = Retriever()

        self.client = Client(
            host="http://localhost:11434"
        )

        self.model = "llama3"

    def ask(
        self,
        question: str
    ):

        documents = self.retriever.search(
            question,
            top_k=5
        )

        context = ""

        for doc in documents:

            context += doc["text"]

            context += "\n\n"

        prompt = f"""
You are an expert Secure Code Review Assistant.

Use ONLY the provided context to answer.

If the answer is not available,
say that the knowledge base
does not contain enough information.

Context:

{context}

Question:

{question}

Answer:
"""

        response = self.client.chat(

            model=self.model,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]

        )

        return {

            "answer": response["message"]["content"],

            "sources": [

                doc["metadata"]["filename"]

                for doc in documents

            ]

        }