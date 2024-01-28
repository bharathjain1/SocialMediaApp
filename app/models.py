from pydantic import BaseModel

class CreateUser(BaseModel):
    user_name:str
    email : str
    phone_no : int
    password : str

class Userlogin(BaseModel):
    email : str
    password : str

class CreatePost(BaseModel):
    post_id : str
    topic : str
    content : str
    timestamp : str






