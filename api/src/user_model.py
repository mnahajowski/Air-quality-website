from datetime import datetime, timedelta
import sqlite3
from jose import jwt, JWTError
from pydantic import BaseModel
from typing import Optional
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
import os

from starlette import status

SECRET_KEY = os.getenv("JWT_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    access_level: Optional[int] = None


class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(username: str):
    """
    Retrieve a specific user from the database
    :param username: username
    :return: requested user data, or None
    """
    file_path = os.path.normpath(os.path.join(os.path.dirname(__file__), os.pardir, 'users.db'))
    connection = sqlite3.connect(file_path)
    result = connection.execute(f"""SELECT * FROM Users WHERE username = '{username}'""")
    user = [{"username": username, "email": email, "full_name": full_name, "access_level": access_level,
             "hashed_password": hashed_password} for username, email, full_name, access_level, hashed_password
            in result]

    if user:
        user_dict = user[0]
        return UserInDB(**user_dict)


def authenticate_user(username: str, password: str):
    """
    Authenticate user by password
    :param username: username
    :param password: provided password
    :return: user or False
    """
    user = get_user(username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    Create an access token for a specific user
    :param data: token data
    :param expires_delta: expiry date
    :return: encoded jwt token
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    Get user from token
    :param token: jwt token
    :return: user or HTTPException 401 is raised
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user
