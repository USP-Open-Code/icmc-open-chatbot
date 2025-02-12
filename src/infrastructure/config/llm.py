from .settings import settings

from langchain_ollama.llms import OllamaLLM
from langchain_openai import ChatOpenAI


class LLM:
    def __new__(cls, model_name: str):
        try:
            if model_name == "ollama":
                return OllamaLLM(
                    model=settings.MODEL_NAME,
                    base_url=settings.MODEL_URL,
                    temperature=settings.MODEL_TEMPERATURE
                )

            elif model_name == "openai":
                return ChatOpenAI(
                    model=settings.MODEL_NAME,
                    base_url=settings.MODEL_URL,
                    temperature=settings.MODEL_TEMPERATURE,
                    api_key=settings.MODEL_API_KEY
                )
            # More models can be added here

            raise ValueError(f"Model {model_name} not supported")

        except Exception as e:
            raise ValueError(
                f"Problem instantiating the model {model_name}: {e}"
            )
