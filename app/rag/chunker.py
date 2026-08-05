from langchain_text_splitters import RecursiveCharacterTextSplitter


class DocumentChunker:

    @staticmethod
    def split(documents):

        splitter = RecursiveCharacterTextSplitter(

            chunk_size=1000,

            chunk_overlap=200,

            separators=[
                "\n\n",
                "\n",
                ". ",
                " "
            ]
        )

        return splitter.split_documents(documents)