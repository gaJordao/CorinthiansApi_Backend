from fastapi import APIRouter

from api.v1.endpoints import titulos
from api.v1.endpoints import jogadores
from api.v1.endpoints import titulos_jogadores

api_router = APIRouter()

api_router.include_router(jogadores.router, prefix="/jogadores", tags=["jogadores"])
api_router.include_router(titulos.router, prefix="/titulos", tags=["titulos"])
api_router.include_router(titulos_jogadores.router, prefix="/titulos_jogadores", tags=["titulos_jogadores"])
