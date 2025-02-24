import uuid
import chromadb
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

from src.infrastructure.config import settings
from typing import List, Optional


class ChromaDB:
    def __init__(self):
        self.host = settings.CHROMA_HOST
        self.port = settings.CHROMA_PORT
        self.collection = None
        try:
            self.client = self._connect()
        except Exception:
            raise ConnectionError("Failed to connect to ChromaDB")

    def _connect(self):
        client = chromadb.HttpClient(host=self.host, port=self.port)
        return client

    def _create_collection(self, collection_name: str = None):
        self.collection = self.client.get_or_create_collection(
            name=collection_name or self.collection
        )
        return self.collection

    def as_retriever(self, collection_name: str = None) -> dict:
        """
        Método que consulta a vector store para consultar os documentos
        que podem ajudar a responder a pergunta do usuário.
        """
        vector_store = Chroma(
            client=self.client,
            collection_name=collection_name or self.collection,
            embedding_function=OllamaEmbeddings(model=settings.EMBEDDING_MODEL)
        )
        retriever = vector_store.as_retriever()

        return {
            "title": "Document Retriever",
            "description": """
                Método que consulta a vector store para consultar os documentos
                que podem ajudar a responder a pergunta do usuário.
                """,
            "type": "object",
            "properties": {
                "search_type": {
                    "type": "string",
                    "description": "Type of search to perform",
                    "enum": ["similarity", "mmr", "similarity_score_threshold"]
                },
                "k": {
                    "type": "integer",
                    "description": "Number of documents to retrieve",
                    "default": 4
                }
            },
            "retriever": retriever
        }

    async def add_documents(
        self,
        documents: List[str],
        collection_name: str,
        metadatas: Optional[List[dict]] = None,
    ):
        if not self.collection:
            self.collection = self._create_collection(collection_name)
        return self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=[str(uuid.uuid4()) for _ in enumerate(documents)]
        )

    async def list_collections(self):
        return self.client.list_collections()

    async def list_documents(
        self,
        collection_name: str
    ):
        if collection := self.client.get_collection(collection_name):
            return collection.get()
        return []

    async def query_documents(
        self,
        query_text: str,
        collection_name: str,
        n_results: int = 5,
        where: Optional[dict] = None
    ):
        if not self.collection:
            self.collection = self._create_collection(collection_name)
        return self.collection.query(
            query_texts=[query_text],
            n_results=n_results,
            where=where
        )

    async def delete_documents(
        self,
        ids: List[str],
        collection_name: str
    ):
        if not self.collection:
            self.collection = self._create_collection(collection_name)
        return self.collection.delete(ids=ids)

    async def close(self):
        if self.client:
            self.client.reset()
