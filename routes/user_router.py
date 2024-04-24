from typing import Union
from fastapi import APIRouter, Body

from models.user import ResponseModel, UserModel
from repositories.user_repository import UserRepository


user_router = APIRouter(
    prefix='/users',
    tags = ['users']
)

@user_router.get("/")
async def read_root():
    return {"Message": "Users"}

@user_router.post("/")
async def create_user(user: UserModel = Body(...)):
    return ResponseModel(await UserRepository.create_user(user), "User created")