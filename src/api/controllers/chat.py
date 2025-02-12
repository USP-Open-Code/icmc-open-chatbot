from src.infrastructure.database import MongoDB, get_service_details
from src.infrastructure.config import LLM
from src.services import CustomChat


async def new_message(
    db: MongoDB,
    model: LLM,
    message: str,
    service_name: str,
) -> str:

    if service_details := get_service_details(service_name, db):
        prompt = service_details["prompt"]
    else:
        prompt = "You are a helpful assistant. Be kind!"

    chat = CustomChat(
        model=model,
        sys_prompt=prompt
    )
    response = await chat(message)
    return response
