# app/v1/schema/schema_transaccion_cliente.py

from pydantic import BaseModel
from decimal import Decimal

class TransaccionClienteDetalle(BaseModel):
    fecha_giro: str
    descripcion: str
    pais_destino: str
    tasa: str
    moneda_cambio: str
    envia: str
    monto_enviado: Decimal
    quien_recibe: str
    monto_recibido: str

    class Config:
        from_attributes = True
