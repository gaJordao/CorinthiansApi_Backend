from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.all_models import JogadoresModel, TitulosModel, TitulosJogadoresModel
from schemas.jogadores_schema import JogadoresSchema
from core.deps import get_session

from sqlalchemy.orm import selectinload
from sqlalchemy.future import select

router = APIRouter()


def get_db_session():
    async def _get_db_session(db: AsyncSession = Depends(get_session)):
        async with db as session:
            yield session

    return _get_db_session()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=JogadoresSchema)
async def post_jogador(jogador: JogadoresSchema, db: AsyncSession = Depends(get_session)):
    novo_jogador = JogadoresModel(**jogador.dict())
    db.add(novo_jogador)
    await db.commit()

    return novo_jogador


@router.get("/", response_model=List[JogadoresSchema], status_code=status.HTTP_200_OK)
async def get_jogadores(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(JogadoresModel)
        result = await session.execute(query)
        jogadores = result.scalars().all()

    return jogadores

@router.get("/j1", response_model=List[JogadoresSchema], status_code=status.HTTP_200_OK)
async def get_jogadores_com_titulos(session: AsyncSession = Depends(get_session)):
    async with session as async_session:
        # Consulta para obter jogadores com seus títulos
        query = (
            select(JogadoresModel)
            .options(selectinload(JogadoresModel.titulos))
            .join(TitulosJogadoresModel)
            .join(TitulosModel)
        )
        result = await async_session.execute(query)
        jogadores = result.scalars().all()

    # Construindo a resposta
    jogadores_com_titulos = []
    for jogador in jogadores:
        titulos = [titulo.nome_titulo for titulo in jogador.titulos]
        jogador_dict = {
            "id": jogador.id,
            "nome": jogador.nome,
            "apelido": jogador.apelido,
            "posicao": jogador.posicao,
            "atuando": jogador.atuando,
            "pais": jogador.pais,
            "numero": jogador.numero,
            "foto": jogador.foto,
            "titulos": titulos
        }
        jogadores_com_titulos.append(jogador_dict)

    return jogadores_com_titulos






@router.get("/{jogador_id}", response_model=JogadoresSchema, status_code=status.HTTP_200_OK)
async def get_jogador(jogador_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(JogadoresModel).filter(JogadoresModel.id == jogador_id)
        result = await session.execute(query)
        jogador = result.scalar_one_or_none()

    if jogador:
        return jogador
    else:
        raise HTTPException(detail="Jogador não encontrado", status_code=status.HTTP_404_NOT_FOUND)


@router.put("/{jogador_id}", response_model=JogadoresSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_jogador(jogador_id: int, jogador: JogadoresSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(JogadoresModel).filter(JogadoresModel.id == jogador_id)
        result = await session.execute(query)
        jogador_up = result.scalar_one_or_none()

    if not jogador_up:
        raise HTTPException(detail="Jogador não encontrado", status_code=status.HTTP_404_NOT_FOUND)

    jogador_dict = jogador.dict(exclude_unset=True)
    for field, value in jogador_dict.items():
        setattr(jogador_up, field, value)

    await db.commit()

    return jogador_up


@router.delete("/{jogador_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_jogador(jogador_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(JogadoresModel).filter(JogadoresModel.id == jogador_id)
        result = await session.execute(query)
        jogador_del = result.scalar_one_or_none()

    if not jogador_del:
        raise HTTPException(detail="Jogador não encontrado", status_code=status.HTTP_404_NOT_FOUND)

    session.delete(jogador_del)
    await session.commit()
