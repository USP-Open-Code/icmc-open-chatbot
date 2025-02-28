from src.infrastructure.database import MongoDB


def get_service_details(service_name: str, database: MongoDB):
    if service_name:
        collection = database.get_collection("services")
        response = collection.find_one({"name": service_name})

        if response:
            return response

    return None


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
