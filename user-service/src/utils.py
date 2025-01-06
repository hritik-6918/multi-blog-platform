import bcrypt
import jwt
import os
from datetime import datetime, timedelta

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def generate_jwt(payload):
    secret = os.getenv("JWT_SECRET")
    expiration = datetime.utcnow() + timedelta(hours=1)
    payload['exp'] = expiration
    return jwt.encode(payload, secret, algorithm="HS256")

def decode_jwt(token):
    secret = os.getenv("JWT_SECRET")
    try:
        payload = jwt.decode(token, secret, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
       return {"message": "Token expired"}
    except jwt.InvalidTokenError:
       return {"message": "Invalid token"}