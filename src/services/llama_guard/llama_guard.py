from langchain_ollama.llms import OllamaLLM
from src.infrastructure.config import settings


class LlamaGuard:
    def __init__(self) -> None:
        try:
            self.llm = OllamaLLM(
                model=settings.LLAMA_GUARD_MODEL,
                base_url=settings.MODEL_URL,
            )
        except:
            return None

    def __call__(self, message: str):
        response = self.llm.invoke(message)
        return True if response == "safe" else False
