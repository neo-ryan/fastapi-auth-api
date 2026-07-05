from bcrypt import hashpw, checkpw, gensalt

def hash_password(password:str):
    return hashpw(password.encode('utf-8'), gensalt())

def check_pass(password, hashed):
    return checkpw(password, hashed)