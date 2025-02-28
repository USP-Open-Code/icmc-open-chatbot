from fastapi import FastAPI

from src.infrastructure.database import MongoDB, ChromaDB
from src.infrastructure.config.llm import LLM
from src.services.llama_guard import LlamaGuard
from src.services.crag import CRAG

from src.api.routes import chat_router, files_router, crag_router


def create_app():
    app = FastAPI()

    # defining API variables
    app.database = MongoDB()
    app.llm = LLM()
    app.llama_guard = LlamaGuard()
    app.vector_store = ChromaDB()
    app.crag = CRAG()  # Corrective RAG

    # including routes
    app.include_router(chat_router)
    app.include_router(files_router)
    app.include_router(crag_router)

    return app
