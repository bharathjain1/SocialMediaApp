from pydantic import BaseModel

class CreateUser(BaseModel):
    user_name:str
    email : str
    phone_no : int
    password : str

class Userlogin(BaseModel):
    username : str
    password : str

class CreatePost(BaseModel):
    topic : str
    content : str






