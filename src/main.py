from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.api.routes import chat_router
from src.database.mongodb.connector import MongoDB


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    app.mongodb = MongoDB()
    await app.mongodb.connect(db_name="crag_app")
    yield
    # Shutdown
    await app.mongodb.close()


def create_app():
    # app = FastAPI(lifespan=lifespan)
    app = FastAPI()
    app.include_router(chat_router)
    return app
