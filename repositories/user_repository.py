from database import user_collection, user_helper
from models.user import UserModel


class UserRepository:
    async def create_user(user: UserModel) -> dict:
        new_user = await user_collection.insert_one(
            user.model_dump(by_alias=True, exclude=["id"])
        )
        created_user = await user_collection.find_one(
            {"_id": new_user.inserted_id}
        )

        return user_helper(created_user)