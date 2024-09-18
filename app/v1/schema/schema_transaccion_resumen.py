# app/v1/schema/schema_transaccion_resumen.py

from pydantic import BaseModel
from decimal import Decimal

class TransaccionResumen(BaseModel):
    total_monto_enviado: Decimal
    porcentaje: Decimal
    fecha_giro: str
    moneda: str
    agente: str

    class Config:
        from_attributes = True
