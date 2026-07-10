from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentChunker:
    """
    Splits extracted documents into smaller chunks
    for embedding generation.
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200
    ):

        self.splitter = RecursiveCharacterTextSplitter(

            chunk_size=chunk_size,

            chunk_overlap=chunk_overlap,

            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]

        )

    def chunk_documents(self, documents):

        chunks = []

        for document in documents:

            text = document["text"]

            metadata = document["metadata"]

            pieces = self.splitter.split_text(text)

            for index, piece in enumerate(pieces):

                chunks.append({

                    "text": piece,

                    "metadata": {

                        **metadata,

                        "chunk_id": index

                    }

                })

        return chunks