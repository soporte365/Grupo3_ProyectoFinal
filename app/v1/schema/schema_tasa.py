from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class Tasa(BaseModel):

    ta_descri: str
    ta_mond: str
    ta_cambio: Decimal
    ta_act: str
    ta_fecha: datetime = datetime.now()
