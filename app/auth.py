import jwt
from cryptography.fernet import Fernet
from datetime import datetime, timedelta

key = b'tO9ZK4zdMaGEKCsPMj4mnzQPbDqGd7ft1L4S5qOF_rI='
f = Fernet(key)

def encrypt_password(password):
    passw = f.encrypt(password.encode())
    return passw

def decrypt_password(password):
    passw = f.decrypt(password)
    return passw.decode()


# Secret key for JWT token
SECRET_KEY = 'cfsgXwMwMGVZ3qoO4DZBNZARNQGf57xvOej-I8ZCxDs='
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_jwt_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")  
    return encoded_jwt

def verify_access_token(token:str):
    try:
        if "Bearer" in token:
            token = token.split(" ")[1]
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        id:str = payload.get("sub")
        if id is None:
            raise Exception("Credential execption")
    except Exception as e:
        print(e)
        raise Exception("Credential execption")
    return id
