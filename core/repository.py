from json import load, dump
from pathlib import Path
from app.core.security import hash_password, check_pass
from app.models.users import UserBase, UserCreate, UserOut, UserLogin

BASE_DIR = Path(__file__).parent / 'users.json'

async def get_users():
    with open(BASE_DIR, 'r') as f:
        return load(f)
    
async def register(user_data:UserCreate):
    data = await get_users()
    maximum_id = max(data, key=lambda x:x['id'])['id'] if len(data) > 0 else 0
    
    dumped_data = user_data.model_dump()
    hashed = hash_password(dumped_data['password'])
    dumped_data['password'] = hashed.decode('utf-8')
    dumped_data['id'] = maximum_id + 1
    
    data.append(dumped_data)
    
    with open(BASE_DIR, 'w') as f:
        dump(data, f, indent=2)
        return data

async def login(user:UserLogin):
    data = await get_users()
    
    for u in data:
        if user.email == u['email']:
            if check_pass(user.password.encode('utf-8'), u['password'].encode('utf-8')):
                return True
            else:
                return False
        return '401'
            