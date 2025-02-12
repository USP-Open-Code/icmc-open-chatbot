from fastapi import FastAPI

from src.infrastructure.database import MongoDB
from src.api.routes import chat_router
from src.infrastructure.config import settings
from src.infrastructure.config.llm import LLM


def create_app():
    app = FastAPI()

    # defining API variables
    app.database = MongoDB(db_name=settings.MONGO_DB)
    app.llm = LLM(model_name=settings.MODEL)

    # app.vector_store = ChromaDB()
    # app.llm = choose_model(model_name=settings.MODEL)

    # including routes
    app.include_router(chat_router)

    return app
