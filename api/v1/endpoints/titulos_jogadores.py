from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload  
from models.all_models import JogadoresModel, TitulosModel, TitulosJogadoresModel
from schemas.titulos_jogadores_schema import TitulosJogadoresSchema
from core.deps import get_session

router = APIRouter()

@router.get("/", response_model=List[dict], status_code=status.HTTP_200_OK)
async def get_titulos_jogadores(session: AsyncSession = Depends(get_session)):
    async with session as async_session:
        # Consulta para obter dados de TitulosJogadoresModel com dados de jogador e título
        query = (
            select(TitulosJogadoresModel)
            .options(selectinload(TitulosJogadoresModel.jogador), selectinload(TitulosJogadoresModel.titulo))
        )
        result = await async_session.execute(query)
        titulos_jogadores = result.scalars().all()

    if not titulos_jogadores:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum título de jogador encontrado")

    # Criar uma lista para armazenar os resultados finais
    response_data = []

    # Iterar sobre os resultados e criar um dicionário com os dados necessários
    for titulo_jogador in titulos_jogadores:
        jogador_info = {
            "id_jogador": titulo_jogador.jogador.id,
            "nome_jogador": titulo_jogador.jogador.nome,
            "id_titulo": titulo_jogador.titulo.id,
            "nome_titulo": titulo_jogador.titulo.nome_titulo,
            "local_disputa": titulo_jogador.titulo.local_disputa,
            "organizador": titulo_jogador.titulo.organizador,
            "foto": titulo_jogador.titulo.foto
        }
        response_data.append(jogador_info)

    return response_data
