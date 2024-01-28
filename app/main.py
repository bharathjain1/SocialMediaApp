import hashlib
from http import HTTPStatus

from fastapi import FastAPI,Response
from models import CreatePost, CreateUser, Userlogin
from services.create_user import User
from auth import encrypt_password


app = FastAPI()


@app.post("/Createuser/")
def create_user(user:CreateUser):
    '''
    Whatever data we are getting
    via request is to be stored 
    inside the db.
    '''
    user_name = user.user_name
    email = user.email
    phone_no = user.phone_no
    password = user.password
    if user_name and email and phone_no and password:
        password = encrypt_password(password)
        usr = User(user_name,password,email,phone_no)
        usr.create_user
        return Response(status_code=HTTPStatus.OK,message="SuccessFully logged in")
    return Response(status_code=HTTPStatus.BAD_REQUEST,message="user_name or email or phone"
                                                                "no or password is not given")

@app.post("/Userlogin")
def user_login(login_user:Userlogin):
    '''
    We will validate the password and username
    along with the tokenization.
    '''
    pass

@app.post("/{username}/Createpost")
def create_post(username:str,post:CreatePost):
    '''
    we will create a post based on text content
    and then store it in db.
    '''
    pass

@app.get("/listuser")
def list_users():
    '''
    We will list out the users.
    '''
    pass

@app.get("/{username}/listpost")
def list_post(username:str):
    '''
    we will list out all the posts done by user.
    '''
    pass

@app.delete("/{post_id}/deletepost")
def delete_post(post_id:str):
    '''
    we will be deleting the given post id.
    '''
    pass

@app.put("/{post_id}/updatepost")
def update_post(post_id:str):
    '''
    we will update the post given post_id and body.
    '''
    pass

@app.get("/{username}/deleteuser")
def delete_user(username:str):
    '''
    we will be deleting the particular user.
    '''
    pass

