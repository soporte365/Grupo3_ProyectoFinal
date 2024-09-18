# app/v1/schema/schema_emisor_receptor.py

from pydantic import BaseModel

class EmisorReceptorDetalle(BaseModel):
    documento_emisor: str
    nombre_emisor: str
    e_telf: str
    documento_beneficiario: str
    nombre_beneficiario: str
    r_telf: str
    tipo_cuenta: str
    numero_cuenta: str
    banco: str

    class Config:
        from_attributes = True
