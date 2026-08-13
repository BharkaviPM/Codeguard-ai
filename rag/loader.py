from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


class PDFLoader:

    def __init__(self, pdf_root: str):
        self.pdf_root = Path(pdf_root)

    def load_documents(self):
        docs = []

        for pdf in self.pdf_root.rglob("*.pdf"):
            try:
                loader = PyPDFLoader(str(pdf))
                docs.extend(loader.load())
                print(f"Loaded: {pdf.name}")
            except Exception as e:
                print(f"Failed: {pdf} -> {e}")

        return docs