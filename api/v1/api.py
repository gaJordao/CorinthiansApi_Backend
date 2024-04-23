from fastapi import APIRouter

from api.v1.endpoints import titulos
from api.v1.endpoints import jogadores

api_router = APIRouter()

api_router.include_router(jogadores.router, prefix="/jogadores", tags=["jogadores"])
api_router.include_router(titulos.router, prefix="/titulos", tags=["titulos"])
