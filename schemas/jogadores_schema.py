from typing import Optional
from pydantic import BaseModel as SCBaseModel

class JogadoresSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str
    apelido: str
    posicao: str
    atuando: bool
    pais:str
    numero: str
    foto: str

    class Config:
        orm_mode = True