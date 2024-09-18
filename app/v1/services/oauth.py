from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import Optional
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.v1.database.db import  get_db
from app.v1.models.model import Usuarios

# Secreto para firmar los tokens
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Configuración de bcrypt para hash de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Configuración de OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Modelo para los datos del token
class Token(BaseModel):
    access_token: str
    token_type: str


# Modelo para los datos del token
class TokenData(BaseModel):
    username: Optional[str] = None


# Modelo para los datos del usuario
class User(BaseModel):
    username: str
    email: Optional[str] = None
    disabled: Optional[bool] = None


# Modelo para los datos del usuario en la base de datos
class UserInDB(User):
    hashed_password: str


# Verificación de contraseña
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


# Hash de la contraseña
def get_password_hash(password):
    return pwd_context.hash(password)


# Función para obtener el usuario de la base de datos
def get_user(db: Session, email: str):
    return db.query(Usuarios).filter(Usuarios.u_email == email).first()


# Función para autenticar al usuario
def authenticate_user(db: Session, email: str, password: str):
    user = get_user(db, email)
    if not user:
        return False
    if not verify_password(password, user.u_pass):
        return False
    return user


# Función para crear el token de acceso
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Dependencia para obtener el usuario actual basado en el token
async def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")  # Asegúrate de que este campo sea correcto
        if email is None:
            raise credentials_exception
        token_data = TokenData(username=email)
    except JWTError:
        raise credentials_exception
    user = get_user(db, email=token_data.username)
    if user is None:
        raise credentials_exception
    return user
