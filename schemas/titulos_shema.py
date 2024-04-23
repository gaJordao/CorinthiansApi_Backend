from typing import Optional
from pydantic import BaseModel as SCBaseModel

class TitulosSchema(SCBaseModel):
    id: Optional[int] = None
    nome_titulo: str
    local_disputa: str
    organizador: str
    foto: str

    class Config:
        orm_mode = True