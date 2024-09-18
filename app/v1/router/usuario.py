from http.client import HTTPException

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.v1.database.db import get_db
from app.v1.models import model
from app.v1.models.model import Usuarios as UserModel, Usuarios
from app.v1.schema.schema_usuario import User


router = APIRouter(
    prefix="/users",  # Prefijo para todas las rutas de usuarios
    tags=["Users"],  # Etiqueta para agrupar las rutas en la documentación de Swagger
)


# Ruta para obtener usuarios
@router.get("/all")
def get_user(db: Session = Depends(get_db)):
    users = db.query(model.Usuarios).all()
    return users


# Ruta para obtener usuarios por id
@router.get("/User_id/{usuario_id}", response_model=User)
def read_user(usuario_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id_user == usuario_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return user


# Ruta para crear nuevos usuarios
@router.post("/ create", response_model=User)
def create_users(user: User, db: Session = Depends(get_db)):
    db_usuario = UserModel(**user.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


## Ruta para actualizar usuairos


@router.put("/users/{usuario_id}", response_model=User)
def update_user(usuario_id: int, user_update: User, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id_user == usuario_id).first()

    if user is None:
        raise HTTPException(status_code=404, detail="Usuario not found")

    for key, value in user_update.dict().items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)

    return user


# Ruta para eliminar usuarios
@router.delete("/users/{usuario_id}", response_model=User)
def delete_users(usuario_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.id_user == usuario_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario not found")

    db.delete(user)
    db.commit()
    return user
