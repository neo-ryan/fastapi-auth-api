from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from app.models.users import UserBase, UserCreate, UserOut, UserLogin
from app.services import user_function

router = APIRouter(prefix='/auth')

auth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/login')

@router.post('/register')
async def register(user_data:UserCreate):
    return await user_function.register(user_data)

@router.post('/login')
async def login(user:UserLogin):
    return await user_function.login(user)

@router.get('/users/me')
async def current_user(token:str = Depends(auth2_scheme)):
    return await user_function.current_user(token)

@router.post('/refresh')
async def refresh(refresh_token):
    return await user_function.refresh(refresh_token)

@router.post('/logout')
async def logout(refresh_token:str):
    return await user_function.logout(refresh_token)

#@router.put('/users/me')
#async def update_user():
#    pass

#@router.put('/users/me/password')
#async def change_password():
#    #pass