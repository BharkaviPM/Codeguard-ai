from chromadb import PersistentClient

from app.core.config import CHROMA_DB


class VectorStore:

    _client = None

    _collection = None

    @classmethod
    def get_collection(cls):

        if cls._client is None:

            cls._client = PersistentClient(

                path=str(CHROMA_DB)

            )

            cls._collection = cls._client.get_or_create_collection(

                name="secure_coding"

            )

        return cls._collection