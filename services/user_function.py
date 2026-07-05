from app.models.users import UserCreate, UserBase, UserOut, UserLogin
from app.core import repository
from fastapi import HTTPException

async def register(user_data:UserCreate):
    return await repository.register(user_data)

async def login(user:UserLogin):
    response = await repository.login(user)
    if response == '401':
        raise HTTPException(status_code=401)
    elif response == False:
        return False
    else:
        return response

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