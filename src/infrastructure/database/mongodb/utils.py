from src.infrastructure.database import MongoDB

from typing import Dict


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


async def add_message_to_history(
    message: Dict[str, str], user_id: str, database: MongoDB
) -> None:
    try:
        if message and user_id:
            history = await database.find(
                filter_query={"user_id": user_id},
                collection_name="chat_history"
            )

            if history:
                history[0]["history"].append(message[0])
                history[0]["history"].append(message[1])

                _ = await database.update_one(
                    collection_name="chat_history",
                    filter_query={"user_id": user_id},
                    update={"$set": {"history": history[0]["history"]}}
                )

            else:
                _ = await database.insert_one(
                    collection_name="chat_history",
                    document={
                        "user_id": user_id,
                        "history": [message[0], message[1]]
                    }
                )

    except Exception as e:
        raise ValueError(f"Error adding message to history: {e}")
