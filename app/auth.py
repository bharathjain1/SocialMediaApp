import jwt
from cryptography.fernet import Fernet

# key = Fernet.generate_key()
key = "tO9ZK4zdMaGEKCsPMj4mnzQPbDqGd7ft1L4S5qOF_rI="
cipher_suite = Fernet(key)

def encrypt_password(password):
    password = cipher_suite.encrypt(password)
    return password

def decrypt_password(password):
    password = cipher_suite.decrypt(password)
    return password
