# schemas.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# class EmisorBase(BaseModel):
#     e_docu: str
#     e_nomb: str
#     e_apel: str
#     e_telf: str
#     e_mail: Optional[str] = None


class EmisorCreate(BaseModel):
    e_docu: str
    e_nomb: str
    e_apel: str
    e_telf: str
    e_mail: Optional[str] = None


class EmisorUpdate(BaseModel):
    e_docu: Optional[str] = None
    e_nomb: Optional[str] = None
    e_apel: Optional[str] = None
    e_telf: Optional[str] = None
    e_mail: Optional[str] = None
