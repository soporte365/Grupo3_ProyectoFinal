# schemas.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ReceptorBase(BaseModel):
    r_docu: str
    r_nomb: str
    r_apel: str
    r_telf: Optional[str] = None
    r_email: Optional[str] = None
    r_tipcuen: str
    r_numcuen: str
    id_bancos: int


class ReceptorCreate(ReceptorBase):
    pass


class ReceptorUpdate(BaseModel):
    r_docu: Optional[str] = None
    r_nomb: Optional[str] = None
    r_apel: Optional[str] = None
    r_telf: Optional[str] = None
    r_email: Optional[str] = None
    r_tipcuen: Optional[str] = None
    r_numcuen: Optional[str] = None
    id_bancos: Optional[int] = None
