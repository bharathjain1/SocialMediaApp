from pydantic import BaseModel

class CreateUser(BaseModel):
    user_name:str
    email : str
    phone_no : int
    password : str

class Userlogin(BaseModel):
    user_name : str
    password : str

class CreatePost(BaseModel):
    user_name : str
    topic : str
    content : str






