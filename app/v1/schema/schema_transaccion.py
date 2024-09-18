# app/v1/schema/schema_transaccion.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from decimal import Decimal

# Esquema base para definir los atributos comunes de 'transaccion'
class TransaccionBase(BaseModel):
    t_fecha: Optional[datetime] = None
    t_monte: Optional[Decimal] = None
    t_montr: Optional[Decimal] = None
    t_descrip: Optional[str] = None
    t_estado: Optional[str] = None
    id_user: Optional[int] = None
    id_tasa: Optional[int] = None
    id_emisor: Optional[int] = None
    id_receptor: Optional[int] = None
    id_pais: Optional[int] = None

# Esquema para la creación de una nueva transacción
class TransaccionCreate(TransaccionBase):
    pass

    class Config:
        from_attributes = True  # Ajuste para Pydantic v2

# Esquema para la actualización de una transacción existente
class TransaccionUpdate(BaseModel):
    t_fecha: Optional[datetime] = None
    t_monte: Optional[Decimal] = None
    t_montr: Optional[Decimal] = None
    t_descrip: Optional[str] = None
    t_estado: Optional[str] = None
    id_user: Optional[int] = None
    id_tasa: Optional[int] = None
    id_emisor: Optional[int] = None
    id_receptor: Optional[int] = None
    id_pais: Optional[int] = None

# Esquema para la representación de una transacción completa con todos los campos
class Transaccion(TransaccionBase):
    id_transac: int  # Campo adicional para incluir el ID de la transacción

    class Config:
        from_attributes = True  # Ajuste para Pydantic v2

