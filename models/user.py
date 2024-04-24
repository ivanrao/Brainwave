from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserModel(BaseModel):
    id: Optional[ObjectId] = Field(alias="_id", default=None)
    name: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)
    model_config = ConfigDict(
        populate_by_name = True,
        arbitrary_types_allowed = True,
        json_schema_extra = {
            "example": {
                "name": "Ivan Rao",
                "email": "ivan.rao@gmail.com",
                "password": "fhgjkhsglfhgsl"
            }
        },
    )

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }