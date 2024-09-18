# app/v1/schema/schema_pais.py

from pydantic import BaseModel

# Esquema base para definir los atributos comunes de 'pais'
class PaisBase(BaseModel):
    p_nomb: str  # Nombre del país, hasta 40 caracteres
    p_mone: str  # Nomenclatura de la moneda del país, hasta 3 caracteres
    p_act: str   # Estado activo o inactivo, 1 caracter

# Esquema para la creación de un nuevo país
class PaisCreate(PaisBase):
    pass  # Hereda los atributos de PaisBase, no se necesitan cambios adicionales

# Esquema para la actualización de un país existente
class PaisUpdate(PaisBase):
    pass  # Hereda los atributos de PaisBase, no se necesitan cambios adicionales

# Esquema para la representación de un país con todos los campos, incluido el ID
class Pais(PaisBase):
    id_pais: int  # Campo adicional para incluir el ID del país

    class Config:
        from_attributes = True  # Usa from_attributes en lugar de orm_mode para Pydantic v2


