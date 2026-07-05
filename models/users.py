from pydantic import BaseModel, Field, EmailStr

class UserBase(BaseModel):
    username:str = Field(max_length=16, min_length=4)
    email:EmailStr

class UserCreate(UserBase):
    password:str = Field(min_length=6, description='Pre-hash password')

class UserOut(UserBase):
    id:int

class UserLogin(BaseModel):
    email:EmailStr
    password:str = Field(min_length=6)
    
class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:int