from datetime import datetime
from langchain_ollama import OllamaLLM
from langchain_openai import ChatOpenAI

from src.services.crag import CRAG
from src.infrastructure.database import MongoDB
from src.infrastructure.database import add_message_to_history


async def contr_new_message(
    message: str,
    user_id: str,
    crag: CRAG,
    llm: ChatOpenAI | OllamaLLM,
    database: MongoDB
) -> str:

    response = await crag.invoke(
        message=message,
        model=llm
    )

    _ = await add_message_to_history(
        message=[
            {
                "role": "user",
                "content": message,
                "timestamp": datetime.now().isoformat()
            },
            {
                "role": "assistant",
                "content": response["messages"],
                "timestamp": datetime.now().isoformat()
            }
        ],
        user_id=user_id,
        database=database
    )

    return response["messages"]
