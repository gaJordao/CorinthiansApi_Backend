from typing import Optional
from pydantic import BaseModel as SCBaseModel
from schemas.jogadores_schema import JogadoresSchema
from schemas.titulos_shema import TitulosSchema

class TitulosJogadoresSchema(SCBaseModel):
    id: int
    jogador: JogadoresSchema
    titulo: TitulosSchema

    class Config:
        orm_mode = True