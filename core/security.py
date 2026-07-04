from bcrypt import hashpw, gensalt

async def hash_password(password:str):
    return hashpw(password.encode('utf-8'), gensalt())