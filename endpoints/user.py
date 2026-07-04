from fastapi import APIRouter
from app.models.users import UserBase, UserCreate, UserOut
from app.services import user_function

router = APIRouter(prefix='/auth')

@router.post('/register')
async def register(user_data:UserCreate):
    return await user_function.register(user_data)

@router.post('/login')
async def login():
    pass

@router.get('/users/me')
async def current_user():
    pass

@router.post('/auth/refresh')
async def refresh():
    pass

@router.post('/auth/logout')
async def logout():
    pass

@router.put('/users/me')
async def update_user():
    pass

@router.put('/users/me/password')
async def change_password():
    pass