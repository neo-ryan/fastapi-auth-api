from json import load, dump
from pathlib import Path
from app.core import security
from app.models.users import UserBase, UserCreate, UserOut

BASE_DIR = Path(__file__).parent / 'users.json'

async def get_users():
    with open(BASE_DIR, 'r') as f:
        return load(f)
    
async def register(user_data:UserCreate):
    data = await get_users()
    dumped_data = user_data.model_dump()
    hashed = await security.hash_password(dumped_data['password'])
    dumped_data['password'] = hashed.decode('utf-8')