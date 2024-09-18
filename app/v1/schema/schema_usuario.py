# schemas.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class User(BaseModel):

    u_nombr: str
    u_email: str
    u_pass: str
    u_act: str
    u_tipo: str
    u_fechcrea: datetime = datetime.now()
    u_fechlogi: datetime = datetime.now()

    class User(BaseModel):
        id: int
        name: str

        class Config:
            from_attributes = True
