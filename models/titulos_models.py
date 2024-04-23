# from core.configs import settings
# from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import relationship
# from sqlalchemy import Table, ForeignKey
# # settings.py

# from sqlalchemy import MetaData

# metadata = MetaData()


# class TitulosModel(settings.DBBaseModel):
#     __tablename__ = "titulos"

#     id: int = Column(Integer(), primary_key=True, autoincrement=True)
#     nome_titulo: str = Column(String(20))
#     local_disputa: str = Column(String(40))
#     organizador: str = Column(String(40))
#     foto: str = Column(String(255))
#     jogadores = relationship("JogadoresModel", secondary="titulos_jogadores", back_populates="titulos")


# titulos_jogadores = Table('titulos_jogadores', settings.metadata,
#     Column('jogador_id', Integer, ForeignKey('jogadores.id')),
#     Column('titulo_id', Integer, ForeignKey('titulos.id'))
# )



    