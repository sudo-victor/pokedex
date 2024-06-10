import math
from typing import Dict, Any

from app.utils.pokemon_helpers import pokemon_mapper
from app.repositories.pokemon_repository import list_pokemons_from_db


async def fetch_pokemons(page: int, limit: int) -> Dict[str, Any]:
    data = list_pokemons_from_db(page, limit)
    pokemons = data["pokemons"]
    total_count = data["total_count"]

    pokemons_with_img = [
        pokemon_mapper(pokemon) for pokemon in pokemons
    ]
    sorted_pokemons = sorted(pokemons_with_img, key=lambda x: x['name'])

    return {
        "count": total_count,
        "result": sorted_pokemons,
        "current_page": page,
        "limit": limit,
        "total_pages": math.ceil(total_count / limit)
    }
