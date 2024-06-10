from sqlalchemy import or_
from app.models.pokemon import Pokemon
from app.models.stat import Stat
from app.database import SessionLocal
from app.utils.pokemon_helpers import pokemon_details_mapper


def get_pokemon_details_from_db(name_or_code: int | str):
    db = SessionLocal()
    try:
        pokemon = db.query(Pokemon).filter(
            or_(Pokemon.code == name_or_code, Pokemon.name == name_or_code)
        ).first()

        if not pokemon:
            return None

        stats = db.query(Stat).filter(Stat.pokemon_id == pokemon.id).all()
        return pokemon_details_mapper(pokemon, stats)
    finally:
        db.close()


def list_pokemons_from_db(page: int, limit: int):
    db = SessionLocal()
    try:
        offset = (page - 1) * limit
        pokemons = db.query(Pokemon).order_by(
            Pokemon.name).offset(offset).limit(limit).all()
        total_count = db.query(Pokemon).count()
        return {
            "pokemons": pokemons,
            "total_count": total_count
        }
    finally:
        db.close()
