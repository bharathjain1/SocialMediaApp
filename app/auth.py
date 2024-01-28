import jwt

from jose import JWTError
from cryptography.fernet import Fernet
from datetime import datetime, timedelta

# key = Fernet.generate_key()
key = "tO9ZK4zdMaGEKCsPMj4mnzQPbDqGd7ft1L4S5qOF_rI="
cipher_suite = Fernet(key)


def encrypt_password(password):
    password = cipher_suite.encrypt(password)
    return password

def decrypt_password(password):
    password = cipher_suite.decrypt(password)
    return password

# Secret key for JWT token
SECRET_KEY = 'cfsgXwMwMGVZ3qoO4DZBNZARNQGf57xvOej-I8ZCxDs='
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_jwt_token(data:dict,expires_delta:ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")  
    return encoded_jwt

def verify_access_token(token:str):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
        id:str = payload.get("username")
        if id is None:
            raise Exception("Credential execption")
    except JWTError as e:
        print(e)
        raise Exception("Credential execption")
    return id
