import os
from motor.motor_asyncio import AsyncIOMotorClient


client = AsyncIOMotorClient(os.environ["MONGODB_URL"])
db = client.get_database(os.environ["DATABASE_NAME"])
user_collection = db.get_collection("users")

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": str(user["name"]),
        "email": str(user["email"])
    }