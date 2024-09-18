from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.v1.database.db import get_db
from app.v1.models.model import Usuarios as UserModel
from app.v1.schema.schema_usuario import User
from app.v1.services.oauth import (
    get_current_user,
    authenticate_user,
    Token,
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from datetime import timedelta


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


# Inicializa el contexto de hashing de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


@router.get("/all")
def get_user(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    return users


@router.get("/User_id/{usuario_id}", response_model=User)
def read_user(
    usuario_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    user = db.query(UserModel).filter(UserModel.id_user == usuario_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return user


@router.post("/create", response_model=User)
def create_users(user: User, db: Session = Depends(get_db)):
    hashed_password = hash_password(user.u_pass)
    db_usuario = UserModel(**{**user.dict(), "u_pass": hashed_password})
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


@router.put("/users/{usuario_id}", response_model=User)
def update_user(usuario_id: int, user_update: User, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id_user == usuario_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="Usuario not found")

    for key, value in user_update.dict().items():
        if key == "u_pass":  # Solo actualiza la contraseña si se ha proporcionado
            value = hash_password(value)
        setattr(user, key, value)

    db.commit()
    db.refresh(user)

    return user


@router.delete("/users/{usuario_id}", response_model=User)
def delete_users(
    usuario_id: int,
    db: Session = Depends(get_db),
    current_user: UserModel = Depends(get_current_user),
):
    user = db.query(UserModel).filter(UserModel.id_user == usuario_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario not found")

    db.delete(user)
    db.commit()
    return user


@router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.u_email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
