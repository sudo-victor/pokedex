from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Pokemon(Base):
    __tablename__ = "pokemons"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True, unique=True)
    name = Column(String, index=True, unique=True)
    types = Column(String)
    abilities = Column(String)
    height = Column(Integer)
    weight = Column(Integer)
    img = Column(String)
    stats = relationship("Stat", back_populates="pokemon")
