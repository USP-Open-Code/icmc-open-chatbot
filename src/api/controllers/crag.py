from langchain_ollama import OllamaLLM
from langchain_openai import ChatOpenAI
from src.services.crag import CRAG


async def contr_new_message(
    message: str,
    crag: CRAG,
    llm: ChatOpenAI | OllamaLLM,
) -> str:
    response = await crag.invoke(
        message=message,
        model=llm
    )
    return response["messages"]
