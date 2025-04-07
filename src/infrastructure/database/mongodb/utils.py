from src.infrastructure.database import MongoDB

from typing import Dict, List


def get_user_details(user_id: str, database: MongoDB) -> dict | None:
    if user_id:
        collection = database.get_collection("users")
        response = collection.find_one({"id": user_id})

        return response


async def block_user(user_id: str, database: MongoDB) -> None:
    if user_id:
        collection = database.get_collection("users")
        collection.insert_one(
            {
                "id": user_id,
                "blocked": True,
                "user": user_id
            }
        )


async def get_messages_history(
    user_id: str,
    database: MongoDB
) -> List[Dict[str, str]]:
    try:
        response = await database.find(
            filter_query={"user_id": user_id},
            collection_name="chat_history"
        )
        return response[0]["history"] if response else []
    except Exception as e:
        raise ValueError(f"Error getting history: {e}")


async def add_message_to_history(
    messages: List[Dict[str, str]], user_id: str, database: MongoDB
) -> None:
    try:
        if messages and user_id:
            history = await database.find(
                filter_query={"user_id": user_id},
                collection_name="chat_history"
            )

            if history:
                _ = await database.update_one(
                    collection_name="chat_history",
                    filter_query={"user_id": user_id},
                    update={"$set": {"history": messages}}
                )

            else:
                _ = await database.insert_one(
                    collection_name="chat_history",
                    document={
                        "user_id": user_id,
                        "history": messages
                    }
                )

    except Exception as e:
        raise ValueError(f"Error adding message to history: {e}")
