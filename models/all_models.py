from sqlalchemy import Column, Integer, ForeignKey, String, Boolean
from sqlalchemy.orm import relationship
from core.configs import settings  # Importe o settings do seu projeto

class TitulosModel(settings.DBBaseModel):
    __tablename__ = "titulos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_titulo = Column(String(20))
    local_disputa = Column(String(40))
    organizador = Column(String(40))
    foto = Column(String(255))

    jogadores = relationship("TitulosJogadoresModel", back_populates="titulo")

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

    # Relacionamento com TitulosJogadoresModel
    titulos = relationship("TitulosJogadoresModel", back_populates="jogador")

class TitulosJogadoresModel(settings.DBBaseModel):
    __tablename__ = "titulos_jogadores"

    id = Column(Integer, primary_key=True, index=True)
    jogador_id = Column(Integer, ForeignKey("jogadores.id"))
    titulo_id = Column(Integer, ForeignKey("titulos.id"))

    jogador = relationship("JogadoresModel", back_populates="titulos")
    titulo = relationship("TitulosModel", back_populates="jogadores")
