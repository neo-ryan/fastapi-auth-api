from app.models.users import UserCreate, UserBase, UserOut, UserLogin
from app.core import repository
from fastapi import HTTPException

async def register(user_data:UserCreate):
    return await repository.register(user_data)

async def login(user:UserLogin):
    return await repository.login(user)
    
async def current_user(token:str):
    return await repository.check_user(token)

async def refresh(refresh_token:str):
    return await repository.refresh(refresh_token)

async def logout(refresh_token:str):
    return await repository.logout(refresh_token)

async def update_user():
    pass

async def change_password():
    pass