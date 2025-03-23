from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # MongoDB
    MONGO_HOST: str = "localhost"
    MONGO_PORT: str = "27017"
    MONGO_DB: str

    # ChromaDB
    CHROMA_HOST: str
    CHROMA_PORT: int = 8000
    CHROMA_DB: str
    INDEX_NAME: str
    VECTOR_DIMENSION: int
    CHUNK_SIZE: int
    CHUNK_OVERLAP: int

    # General Settings
    TIMEZONE: str = "America/Sao_Paulo"
    API_PORT: int

    # LLM
    MODEL: str = "ollama"
    MODEL_NAME: str = "llama3"
    MODEL_URL: str = "http://localhost:11434"
    MODEL_TEMPERATURE: float = 0.2
    MODEL_API_KEY: str = ''
    EMBEDDING_MODEL: str = "llama3"

    # LlamaGuard
    LLAMA_GUARD_MODEL: str = "llama-guard3"
    BASE_URL: str

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
