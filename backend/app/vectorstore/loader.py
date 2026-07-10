from pathlib import Path
import fitz


class DocumentLoader:

    def __init__(self, knowledge_path: str):

        # Convert to an absolute path immediately
        self.knowledge_path = Path(knowledge_path).resolve()

        print(f"Knowledge Base: {self.knowledge_path}")

    def load_documents(self):

        documents = []

        if not self.knowledge_path.exists():
            print("Knowledge base folder does not exist!")
            return documents

        pdfs = list(self.knowledge_path.glob("**/*.pdf"))

        print(f"PDFs Found: {len(pdfs)}")

        for pdf in pdfs:

            print(f"Loading: {pdf}")

            document = self.load_pdf(pdf)

            if document is not None:
                documents.append(document)

        return documents

    def load_pdf(self, pdf_path: Path):

        try:

            with fitz.open(pdf_path) as pdf:

                text = ""

                for page in pdf:
                    text += page.get_text()

            return {
                "text": text,
                "metadata": {
                    "source": pdf_path.parent.name,
                    "filename": pdf_path.name,
                    "path": str(pdf_path)
                }
            }

        except Exception as ex:

            print(f"Error reading {pdf_path}: {ex}")

            return None