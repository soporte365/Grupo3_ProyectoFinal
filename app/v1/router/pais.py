from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text  # Importa la función text de SQLAlchemy
from app.v1.database.db import get_db
from typing import List
from app.v1.schema.schema_pais import Pais, PaisCreate, PaisUpdate

router = APIRouter(
    prefix="/paises",
    tags=["Paises"]
)

@router.get("/", response_model=List[Pais])
def get_paises(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM pais")).fetchall()
    paises = [Pais(id_pais=row[0], p_nomb=row[1], p_mone=row[2], p_act=row[3]) for row in result]
    return paises

@router.get("/{id}", response_model=Pais)
def get_pais(id: int, db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM pais WHERE id_pais = :id"), {"id": id}).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Pais no encontrado")
    pais = Pais(id_pais=result[0], p_nomb=result[1], p_mone=result[2], p_act=result[3])
    return pais

@router.post("/", response_model=Pais)
def create_pais(pais: PaisCreate, db: Session = Depends(get_db)):
    db.execute(
        text("INSERT INTO pais (p_nomb, p_mone, p_act) VALUES (:p_nomb, :p_mone, :p_act)"),
        {"p_nomb": pais.p_nomb, "p_mone": pais.p_mone, "p_act": pais.p_act}
    )
    db.commit()
    result = db.execute(text("SELECT * FROM pais WHERE p_nomb = :p_nomb"), {"p_nomb": pais.p_nomb}).first()
    pais_creado = Pais(id_pais=result[0], p_nomb=result[1], p_mone=result[2], p_act=result[3])
    return pais_creado

@router.put("/{id}", response_model=Pais)
def update_pais(id: int, pais: PaisUpdate, db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM pais WHERE id_pais = :id"), {"id": id}).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Pais no encontrado")

    db.execute(
        text("UPDATE pais SET p_nomb = :p_nomb, p_mone = :p_mone, p_act = :p_act WHERE id_pais = :id"),
        {"p_nomb": pais.p_nomb, "p_mone": pais.p_mone, "p_act": pais.p_act, "id": id}
    )
    db.commit()
    result = db.execute(text("SELECT * FROM pais WHERE id_pais = :id"), {"id": id}).first()
    pais_actualizado = Pais(id_pais=result[0], p_nomb=result[1], p_mone=result[2], p_act=result[3])
    return pais_actualizado

@router.delete("/{id}")
def delete_pais(id: int, db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM pais WHERE id_pais = :id"), {"id": id}).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Pais no encontrado")

    db.execute(text("DELETE FROM pais WHERE id_pais = :id"), {"id": id})
    db.commit()
    return {"message": "Pais eliminado exitosamente"}


