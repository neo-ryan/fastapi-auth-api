from datetime import datetime, timedelta, timezone
from bcrypt import hashpw, checkpw, gensalt
from dotenv import load_dotenv
import jwt, os 

load_dotenv()

KEY = os.getenv('KEY')
ALGORITHM = os.getenv('ALGORITHM')

def make_access_token(data:dict, expires_delta:timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({'exp':expire})
    encoded_jwt = jwt.encode(to_encode, KEY, algorithm=ALGORITHM)
    return encoded_jwt

def hash_password(password:str):
    return hashpw(password.encode('utf-8'), gensalt())

def check_pass(password, hashed):
    return checkpw(password, hashed)

def get_current_user(token:str):
    decoded = jwt.decode(token, key=KEY, algorithms=[ALGORITHM])
    return decoded