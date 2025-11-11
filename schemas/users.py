from pydantic import BaseModel

class UserCreate(BaseModel):
    username:str
    email:str
    password:str

class UserUpdate(BaseModel):
    username:str
    email:str
    password:str

class UserUpdatePassword(BaseModel):
    password:str

class UserLogin(BaseModel):
    email:str
    password:str