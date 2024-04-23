# from core.configs import settings
# from sqlalchemy import Column, Integer, String, Boolean, Float
# from sqlalchemy.orm import relationship

# class JogadoresModel(settings.DBBaseModel):
#     __tablename__ = "jogadores"

#     id: int = Column(Integer(), primary_key=True, autoincrement=True)
#     nome: str = Column(String(30))
#     apelido: str = Column(String(30))
#     posicao: str = Column(String(20))
#     atuando: Boolean = Column(Boolean())
#     pais: str = Column(String(20))
#     numero: str = Column(String(3))
#     foto: str = Column(String(255))
#     titulos = relationship("TitulosModel", back_populates="jogador")