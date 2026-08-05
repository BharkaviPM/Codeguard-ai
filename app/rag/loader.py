from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

from app.core.config import KNOWLEDGE_BASE


class KnowledgeLoader:

    @staticmethod
    def load_documents():

        documents = []

        pdf_folder = Path(KNOWLEDGE_BASE)

        # Search recursively
        pdf_files = list(pdf_folder.rglob("*.pdf"))

        print(f"Knowledge Base Path : {pdf_folder.resolve()}")
        print(f"PDF Files Found : {len(pdf_files)}")

        for pdf in pdf_files:

            print(f"Loading : {pdf.relative_to(pdf_folder)}")

            loader = PyPDFLoader(str(pdf))

            docs = loader.load()

            # Add useful metadata
            for doc in docs:
                doc.metadata["source"] = str(pdf.relative_to(pdf_folder))
                doc.metadata["category"] = pdf.parent.name

            documents.extend(docs)

        return documents