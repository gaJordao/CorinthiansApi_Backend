# titulos_models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship
from core.configs import settings  # Importe o settings do seu projeto

class TitulosModel(settings.DBBaseModel):
    __tablename__ = "titulos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_titulo = Column(String(20))
    local_disputa = Column(String(40))
    organizador = Column(String(40))
    foto = Column(String(255))

    # Relacionamento com jogadores
    jogadores = relationship("JogadoresModel", secondary="titulos_jogadores", back_populates="titulos")

class JogadoresModel(settings.DBBaseModel):
    __tablename__ = "jogadores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(30))
    apelido = Column(String(30))
    posicao = Column(String(20))
    atuando = Column(Boolean)
    pais = Column(String(20))
    numero = Column(String(3))
    foto = Column(String(255))

    # Relacionamento com títulos
    titulos = relationship("TitulosModel", secondary="titulos_jogadores", back_populates="jogadores")

# Tabela de associação para relacionamento muitos para muitos
titulos_jogadores = Table('titulos_jogadores', settings.DBBaseModel.metadata,
    Column('jogador_id', Integer, ForeignKey('jogadores.id')),
    Column('titulo_id', Integer, ForeignKey('titulos.id'))
)
