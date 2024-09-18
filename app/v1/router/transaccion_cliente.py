# app/v1/router/transaccion_cliente.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import List
from app.v1.database.db import get_db
from app.v1.schema.schema_transaccion_cliente import TransaccionClienteDetalle

router = APIRouter(
    prefix="/transacciones-cliente",
    tags=["Transacciones por Cliente"]
)


@router.get("/detalle", response_model=List[TransaccionClienteDetalle])
def get_transacciones_cliente_detalle(db: Session = Depends(get_db)):
    query = text("""
    SELECT 
        tr.t_fecha AS "fecha_giro", 
        tr.t_descrip AS "descripcion", 
        pa.p_nomb AS "pais_destino",
        ta.ta_descri AS "tasa", 
        '1 ' || ta.ta_mond || ' = ' || ta.ta_cambio AS "moneda_cambio", 
        em.e_nomb || ' ' || em.e_apel AS "envia", 
        ROUND(tr.t_monte, 2) AS "monto_enviado", 
        re.r_nomb || ' ' || re.r_apel AS "quien_recibe", 
        ROUND(tr.t_montr, 2) || ' ' || pa.p_mone AS "monto_recibido" 
    FROM transaccion tr
    INNER JOIN usuarios us ON us.id_user = tr.id_user
    INNER JOIN tasas ta ON ta.id_tasa = tr.id_tasa
    INNER JOIN emisor em ON em.id_emisor = tr.id_emisor
    INNER JOIN receptor re ON re.id_receptor = tr.id_receptor
    INNER JOIN pais pa ON pa.id_pais = tr.id_pais
    """)

    result = db.execute(query).fetchall()

    # Mapeo de los resultados a una lista de objetos Pydantic
    transacciones_cliente = [
        TransaccionClienteDetalle(
            fecha_giro=row["fecha_giro"],
            descripcion=row["descripcion"],
            pais_destino=row["pais_destino"],
            tasa=row["tasa"],
            moneda_cambio=row["moneda_cambio"],
            envia=row["envia"],
            monto_enviado=row["monto_enviado"],
            quien_recibe=row["quien_recibe"],
            monto_recibido=row["monto_recibido"]
        )
        for row in result
    ]

    return transacciones_cliente
