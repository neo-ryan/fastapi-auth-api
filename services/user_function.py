from app.models.users import UserCreate, UserBase, UserOut, UserLogin
from app.core import repository
from fastapi import HTTPException

async def register(user_data:UserCreate):
    return await repository.register(user_data)

async def login(user:UserLogin):
    return await repository.login(user)
    
async def current_user():
    pass

async def refresh():
    pass

async def logout():
    pass

async def update_user():
    pass

async def change_password():
    pass