# app/v1/schema/schema_mensaje.py

from pydantic import BaseModel

class Mensaje(BaseModel):
    mensaje: str

    class Config:
        from_attributes = True
