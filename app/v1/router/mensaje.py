# app/v1/router/mensaje.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import List
from app.v1.database.db import get_db
from app.v1.schema.schema_mensaje import Mensaje

router = APIRouter(
    prefix="/mensajes",
    tags=["Mensajes"]
)


@router.get("/transacciones", response_model=List[Mensaje])
def get_mensajes_transacciones(db: Session = Depends(get_db)):
    query = text("""
    SELECT 
        'Ha recibido la cantidad de: ' || ROUND(tr.t_montr, 2) || ' ' || pa.p_mone || 
        ', Enviado por: ' || em.e_nomb || ' ' || em.e_apel || 
        ', el día: ' || tr.t_fecha AS mensaje
    FROM transaccion tr
    INNER JOIN tasas ta ON ta.id_tasa = tr.id_tasa
    INNER JOIN emisor em ON em.id_emisor = tr.id_emisor
    INNER JOIN pais pa ON pa.id_pais = tr.id_pais
    WHERE tr.t_estado = '1';
    """)

    result = db.execute(query).fetchall()
   # PREGUNTAR A RAFA POR QUE EL SQL SI RETORNA SIN EL MAPEO
    # Mapeo de los resultados a una lista de objetos Pydantic
    #mensajes = [Mensaje(mensaje=row["mensaje"]) for row in result]

    return result
