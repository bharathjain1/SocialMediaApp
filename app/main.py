from http import HTTPStatus

from fastapi import FastAPI,HTTPException,Request
from models import CreatePost, CreateUser, Userlogin
from services.create_user import User
from services.create_post import Post
from auth import create_jwt_token, encrypt_password,verify_access_token

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
        usr.create_user()
        return {"status_code":HTTPStatus.OK,
                "message":"SuccessFully logged in"}
    return {"status_code":HTTPStatus.BAD_REQUEST,
            "message":"user_name or email or phoneno or password is not given"}

@app.post("/Userlogin")
def user_login(login_user:Userlogin):
    '''
    We will validate the password and username
    along with the tokenization.
    '''
    if not login_user.user_name or not login_user.password:
        return {"status_code":HTTPStatus.BAD_REQUEST,
            "message":"user_name or password is not given"}
    usr = User(login_user.user_name,login_user.password)
    if not usr.authenicate_user():
         raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            message="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_jwt_token(data={"sub":login_user.user_name})
    return {"jwt_token": access_token, "token_type": "bearer"}


@app.post("/{username}/Createpost")
def create_post(post:CreatePost,authorization_token:str):
    '''
    we will create a post based on text content
    and then store it in db.
    '''
    if not post.user_name:
        return {"status_code":"HTTPStatus.BAD_REQUEST",
                        "message":"username empty"}
    verify_token = verify_access_token(authorization_token)
    if verify_token:
        if not post.content or not post.topic:
            return {"status_code":HTTPStatus.BAD_REQUEST,
                            "message":"either post content or post topic is missing !"}
        pst = Post(post.user_name,post.content)
        pst.create_post()
        return {"status_code":HTTPStatus.OK,
                "message":"SuccessFully created the post"}
    return {"status_code":HTTPStatus.BAD_REQUEST,
            "message":"please check the credentials"}

# @app.get("/listuser")
# def list_users():
#     pass

@app.get("/listpost")
def list_post(req:Request):
    '''
    we will list out all the posts done by user.
    '''
    
    authorization_token = req.headers["Authorization"]
    verify_token = verify_access_token(authorization_token)
    if verify_token:
        ps = Post()
        post_list = ps.list_post()
        return {"status_code":HTTPStatus.OK,
                        "message":post_list}
    return {"status_code":HTTPStatus.BAD_REQUEST,"message":"please check the credentials"}

@app.delete("/{post_id}/deletepost")
def delete_post(post_id:str,req:Request):
    '''
    we will be deleting the given post id.
    '''
    authorization_token = req.headers["Authorization"]
    verify_token = verify_access_token(authorization_token)
    if verify_token:
        ps = Post()
        delete_post = ps.delete_post(post_id)
        print(delete_post,"============================")
        if delete_post:
            return {"status_code":HTTPStatus.OK,
                            "message":"deleted post sucessfully"}
    return {"status_code":HTTPStatus.BAD_REQUEST,"message":"please check the credentials and required parameters"}
    

@app.put("/{post_id}/updatepost")
def update_post(post_id:str,req:Request,updated_content:str):
    '''
    we will update the post given post_id and body.
    '''
    authorization_token = req.headers["Authorization"]
    verify_token = verify_access_token(authorization_token)
    if verify_token:
        ps = Post()
        update_post = ps.update_post(updated_content,post_id)
        if update_post:
            return {"status_code":HTTPStatus.OK,
                    "message":"updated post sucessfully"}
    return {"status_code":HTTPStatus.BAD_REQUEST,"message":"please check the credentials and required parameters"}

@app.get("/{username}/deleteuser")
def delete_user(username:str,password:str,req:Request):
    '''
    we will be deleting the particular user.
    '''
    authorization_token = req.headers["Authorization"]
    verify_token = verify_access_token(authorization_token)
    if verify_token:
        usr = User(username)
        delete_user = usr.delete_user()
        if delete_user:
            return {"status_code":HTTPStatus.OK,
                    "message":"delete user sucessfully"}
    return {"status_code":HTTPStatus.BAD_REQUEST,"message":"please check the credentials and required parameters"}
        
    




