# app/v1/router/emisor_receptor.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import List
from app.v1.database.db import get_db
from app.v1.schema.schema_emisor_receptor import EmisorReceptorDetalle


router = APIRouter(
    prefix="/emisor-receptor",
    tags=["Emisor-Receptor"]
)


@router.get("/detalle", response_model=List[EmisorReceptorDetalle])
def get_emisor_receptor_detalle(db: Session = Depends(get_db)):
    query = text("""
    SELECT 
        em.e_docu AS "documento_emisor", 
        em.e_nomb || ' ' || em.e_apel AS "nombre_emisor",
        em.e_telf,
        re.r_docu AS "documento_beneficiario", 
        re.r_nomb || ' ' || re.r_apel AS "nombre_beneficiario",
        re.r_telf, 
        CASE 
            WHEN re.r_tipcuen='A' THEN 'Cuenta Ahorros' 
            ELSE 'Cuenta Corriente' 
        END AS "tipo_cuenta",
        re.r_numcuen AS "numero_cuenta", 
        b.ba_nom AS "banco"
    FROM emisor em
    INNER JOIN emi_recep emre ON emre.id_emisor = em.id_emisor
    INNER JOIN receptor re ON re.id_receptor = emre.id_receptor
    INNER JOIN bancos b ON b.id_bancos = re.id_bancos
    """)

    result = db.execute(query).fetchall()

    # Mapeo de los resultados a una lista de objetos Pydantic
    detalles = [
        EmisorReceptorDetalle(
            documento_emisor=row["documento_emisor"],
            nombre_emisor=row["nombre_emisor"],
            e_telf=row["e_telf"],
            documento_beneficiario=row["documento_beneficiario"],
            nombre_beneficiario=row["nombre_beneficiario"],
            r_telf=row["r_telf"],
            tipo_cuenta=row["tipo_cuenta"],
            numero_cuenta=row["numero_cuenta"],
            banco=row["banco"]
        ) for row in result
    ]
# NO FUNCIONA LLAMANDO DIRECTO A RESULT COMO EN MENSAJE
    return detalles
