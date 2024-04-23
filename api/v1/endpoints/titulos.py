from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.all_models import TitulosModel
from schemas.titulos_shema import TitulosSchema
from core.deps import get_session

router = APIRouter()



@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TitulosSchema)
async def post_titulo(titulo: TitulosSchema, db: AsyncSession = Depends(get_session)):
    novo_titulo = TitulosModel(nome_titulo=titulo.nome_titulo, local_disputa=titulo.local_disputa, organizador=titulo.organizador, foto=titulo.foto)
    db.add(novo_titulo)
    await db.commit()

    return novo_titulo


@router.get("/", response_model=List[TitulosSchema], status_code=status.HTTP_200_OK)
async def get_titulos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TitulosModel)
        result = await session.execute(query)
        titulos: List[TitulosModel] = result.scalars().all()

        return titulos
    

@router.get("/{titulo_id}", response_model=TitulosSchema, status_code=status.HTTP_200_OK)
async def get_titulo(titulo_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TitulosModel).filter(TitulosModel.id == titulo_id)
        result = await session.execute(query)
        titulo = result.scalar_one_or_none()

        if titulo:
            return titulo
        else:
            raise HTTPException(detail="titulo não encontrado", status_code=status.HTTP_404_NOT_FOUND)
        

@router.put("/{titulo_id}", response_model=TitulosSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_titulo(titulo_id: int, titulo: TitulosSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TitulosModel).filter(TitulosModel.id == titulo_id)
        result = await session.execute(query)
        titulo_up = result.scalar_one_or_none()

        if titulo_up:
            titulo_up.nome_titulo = titulo.nome_titulo
            titulo_up.local_disputa = titulo.local_disputa
            titulo_up.organizador = titulo.organizador
            titulo_up.foto = titulo.foto

            await session.commit()

            return titulo_up
        
        else:
            raise HTTPException(detail="titulo não encontrado", status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/{titulo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_titulo(titulo_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(TitulosModel).filter(TitulosModel.id == titulo_id)
        result = await session.execute(query)
        titulo_del = result.scalar_one_or_none()      

        if titulo_del:
            await session.delete(titulo_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="titulo não encontrado", status_code=status.HTTP_404_NOT_FOUND)