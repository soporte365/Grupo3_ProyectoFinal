# app/v1/router/transaccion_resumen.py
'''

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import List
from app.v1.database.db import get_db
from app.v1.schema.schema_transaccion_resumen import TransaccionResumen

router = APIRouter(
    prefix="/transacciones-resumen",
    tags=["Resumen de Transacciones"]
)


@router.get("/", response_model=List[TransaccionResumen])
def get_transacciones_resumen(db: Session = Depends(get_db)):
    query = text("""
    SELECT
        SUM(tr.t_monte) AS "total_monto_enviado",
        ROUND(SUM(tr.t_monte) * 0.015, 2) AS "porcentaje",
        tr.t_fecha AS "fecha_giro",
        ta.ta_mond AS "moneda",
        us.u_nombr AS "agente"
    FROM transaccion tr
    INNER JOIN usuarios us ON us.id_user = tr.id_user
    INNER JOIN tasas ta ON ta.id_tasa = tr.id_tasa
    WHERE tr.t_estado = '1'
    GROUP BY tr.t_fecha, ta.ta_mond, us.u_nombr
    """)

    result = db.execute(query).fetchall()

    # Mapeo de los resultados a una lista de objetos Pydantic
    resumen = [
        TransaccionResumen(
            total_monto_enviado=row["total_monto_enviado"],
            porcentaje=row["porcentaje"],
            fecha_giro=row["fecha_giro"],
            moneda=row["moneda"],
            agente=row["agente"]
        )
        for row in result
    ]

    return resumen

'''

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from typing import List
from app.v1.database.db import get_db
from app.v1.schema.schema_transaccion_resumen import TransaccionResumen

router = APIRouter(
    prefix="/transacciones-resumen",
    tags=["Resumen de Transacciones"]
)


@router.get("/", response_model=List[TransaccionResumen])
def get_transacciones_resumen(db: Session = Depends(get_db)):
    query = text("""
    SELECT 
        SUM(tr.t_monte) AS total_monto_enviado, 
        ROUND(SUM(tr.t_monte) * 0.015, 2) AS porcentaje, 
        tr.t_fecha AS fecha_giro,  
        ta.ta_mond AS moneda, 
        us.u_nombr AS agente
    FROM transaccion tr
    INNER JOIN usuarios us ON us.id_user = tr.id_user
    INNER JOIN tasas ta ON ta.id_tasa = tr.id_tasa
    WHERE tr.t_estado = '1'
    GROUP BY tr.t_fecha, ta.ta_mond, us.u_nombr
    """)

    result = db.execute(query).fetchall()

    # Convertir los resultados en una lista de diccionarios
    resumen = [
        TransaccionResumen(
            total_monto_enviado=row[0],  # total_monto_enviado
            porcentaje=row[1],  # porcentaje
            #fecha_giro=row[2],  # fecha_giro
            fecha_giro=row[2].strftime('%Y-%m-%d %H:%M:%S'),  # Convertir datetime a string
            moneda=row[3],  # moneda
            agente=row[4]  # agente
        )
        for row in result
    ]

    return resumen



