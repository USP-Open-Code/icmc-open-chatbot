from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # MongoDB
    MONGO_USER: str
    MONGO_PASSWORD: str
    MONGO_HOST: str = "localhost"
    MONGO_PORT: str = "27017"
    MONGO_DB: str

    # ChromaDB
    CHROMA_HOST: str = "localhost"
    CHROMA_PORT: str = "8000"
    CHROMA_DB: str

    # General Settings
    TIMEZONE: str = "America/Sao_Paulo"

    # LLM
    MODEL: str = "ollama"
    MODEL_NAME: str = "llama3"
    MODEL_URL: str = "http://localhost:11434"
    MODEL_TEMPERATURE: float = 0.2
    MODEL_API_KEY: str = ''

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
