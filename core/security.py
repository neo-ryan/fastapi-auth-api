from datetime import datetime, timedelta, timezone
from bcrypt import hashpw, checkpw, gensalt
from dotenv import load_dotenv
import jwt, os 
from fastapi import HTTPException

load_dotenv()

KEY = os.getenv('KEY')
ALGORITHM = os.getenv('ALGORITHM')

def make_access_token(data:dict, expires_delta:timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=30)
    to_encode.update({'exp':expire})
    encoded_jwt = jwt.encode(to_encode, KEY, algorithm=ALGORITHM)
    return encoded_jwt

def make_refresh_token(data:dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=3)
    to_encode.update({'exp':expire})
    return jwt.encode(to_encode, KEY, algorithm=ALGORITHM)

def hash_password(password:str):
    return hashpw(password.encode('utf-8'), gensalt())

def check_pass(password, hashed):
    return checkpw(password, hashed)

def get_current_user(token:str):
    try:
        decoded = jwt.decode(token, key=KEY, algorithms=[ALGORITHM])
        return decoded
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401)

def user_refresh(refresh_token:str, tokens):
    try:
        data = jwt.decode(refresh_token, key=KEY, algorithms=[ALGORITHM])
        if refresh_token in tokens:
            expire = datetime.now(timezone.utc) + timedelta(minutes=30)
            data.update({'exp':expire})
            return jwt.encode(data, KEY, algorithm=ALGORITHM)
        else:
            raise HTTPException(status_code=401)
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401)