from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Stat(Base):
    __tablename__ = "stats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    value = Column(Integer, index=True)
    pokemon_id = Column(Integer, ForeignKey("pokemons.id"))
    pokemon = relationship("Pokemon", back_populates="stats")
