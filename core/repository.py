from json import load, dump
from pathlib import Path
from app.core.security import hash_password, check_pass, make_access_token, get_current_user, make_refresh_token, user_refresh
from app.models.users import UserBase, UserCreate, UserOut, UserLogin
from fastapi import HTTPException
from pydantic import EmailStr

BASE_DIR = Path(__file__).parent / 'users.json'
TOKENS_DIR = Path(__file__).parent / 'tokens.json'

async def get_tokens():
    with open(TOKENS_DIR, 'r') as f:
        return load(f)

async def get_users():
    with open(BASE_DIR, 'r') as f:
        return load(f)
    
async def register(user_data:UserCreate):
    data = await get_users()
    
    maximum_id = max(data, key=lambda x:x['id'])['id'] if len(data) > 0 else 0
    
    dumped_data = user_data.model_dump()
    
    if any(u['email'] == dumped_data['email'] for u in data):
        raise HTTPException(status_code=400, detail='Email was already registered')
    
    hashed = hash_password(dumped_data['password'])
    dumped_data['password'] = hashed.decode('utf-8')
    dumped_data['id'] = maximum_id + 1
    
    data.append(dumped_data)
    
    with open(BASE_DIR, 'w') as f:
        dump(data, f, indent=2)
    
    return UserOut.model_validate(dumped_data)
    

async def login(user:UserLogin):
    data = await get_users()
    tokens = await get_tokens()
    
    for u in data:
        if user.email == u['email']:
            if check_pass(user.password.encode('utf-8'), u['password'].encode('utf-8')):
                data_for_token = {'email':u['email'], 'username':u['username'],'id':u['id']}
                access = make_access_token(data_for_token)
                refresh = make_refresh_token(data_for_token)
                tokens.append(refresh)
                with open(TOKENS_DIR, 'w') as f:
                    dump(tokens, f, indent=2)
                return {'access_token':access, 'refresh_token':refresh}
            else:
                raise HTTPException(status_code=401)
        raise HTTPException(status_code=401)

async def refresh(refresh_token:str):
    tokens = await get_tokens()
    return user_refresh(refresh_token, tokens)

async def check_user(token:str):
    data = await get_users()
    decoded_token = get_current_user(token)
    
    for u in data:
        if u['email'] == decoded_token['email']:
            user = UserOut.model_validate(u)
            return user
    
    raise HTTPException(status_code=401)

async def logout(refresh_token:str):
    tokens = await get_tokens()
    new_tokens_list = [i for i in tokens if i != refresh_token]
    
    if len(new_tokens_list) == len(tokens):
        raise HTTPException(status_code=401)
    
    with open(TOKENS_DIR, 'w') as f:
        dump(new_tokens_list, f, indent=2)
    
    return 'Done'
    