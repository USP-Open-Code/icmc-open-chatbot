from .settings import settings

from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI


class LLM:
    def __new__(cls):
        model_name = settings.MODEL

        if model_name == "ollama":
            model = ChatOllama(
                model=settings.MODEL_NAME,
                base_url=settings.MODEL_URL,
                temperature=settings.MODEL_TEMPERATURE
            )

        elif model_name == "openai":
            model = ChatOpenAI(
                model=settings.MODEL_NAME,
                base_url=settings.MODEL_URL,
                temperature=settings.MODEL_TEMPERATURE,
                api_key=settings.MODEL_API_KEY
            )
        # More models can be added here
        else:
            raise ValueError(f"Model {model_name} not supported")

        _ = cls.ping_model(model)
        return model

    @staticmethod
    def ping_model(model: ChatOllama | ChatOpenAI) -> None:
        try:
            model.invoke("Hello, world!")
        except Exception as e:
            raise ValueError(
                f"Problem pinging the model: {e}"
            )
