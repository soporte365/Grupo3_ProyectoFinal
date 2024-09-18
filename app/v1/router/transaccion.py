# app/v1/router/transaccion.py
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.v1.database.db import get_db
from app.v1.models.model import Transaccion as TransaccionModel  # Importa el modelo SQLAlchemy con un alias
from app.v1.schema.schema_transaccion import Transaccion, TransaccionCreate, \
    TransaccionUpdate  # Importa esquemas Pydantic

router = APIRouter(
    prefix="/transacciones",
    tags=["Transacciones"],
)


@router.get("/", response_model=List[Transaccion])  # Usa el esquema Pydantic, no el modelo SQLAlchemy
def get_transacciones(db: Session = Depends(get_db)):
    """Obtener una lista de todas las transacciones."""
    return db.query(TransaccionModel).all()


@router.get("/{id}", response_model=Transaccion)  # Usa el esquema Pydantic
def get_transaccion(id: int, db: Session = Depends(get_db)):
    """Obtener detalles de una transacción específica por su ID."""
    transaccion = db.query(TransaccionModel).filter(TransaccionModel.id_transaccion == id).first()
    if transaccion is None:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")
    return transaccion


@router.post("/", response_model=Transaccion)  # Usa el esquema Pydantic
def create_transaccion(transaccion: TransaccionCreate, db: Session = Depends(get_db)):
    """Crear una nueva transacción."""
    nueva_transaccion = TransaccionModel(**transaccion.dict())
    db.add(nueva_transaccion)
    db.commit()
    db.refresh(nueva_transaccion)
    return nueva_transaccion


@router.put("/{id}", response_model=Transaccion)  # Usa el esquema Pydantic
def update_transaccion(id: int, transaccion: TransaccionUpdate, db: Session = Depends(get_db)):
    """Actualizar una transacción específica por su ID."""
    transaccion_db = db.query(TransaccionModel).filter(TransaccionModel.id_transaccion == id).first()
    if transaccion_db is None:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")

    for key, value in transaccion.dict(exclude_unset=True).items():
        setattr(transaccion_db, key, value)

    db.commit()
    db.refresh(transaccion_db)
    return transaccion_db


@router.delete("/{id}")
def delete_transaccion(id: int, db: Session = Depends(get_db)):
    """Eliminar una transacción específica por su ID."""
    transaccion = db.query(TransaccionModel).filter(TransaccionModel.id_transaccion == id).first()
    if transaccion is None:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")

    db.delete(transaccion)
    db.commit()
    return {"message": "Transacción eliminada exitosamente"}

