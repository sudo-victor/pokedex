import re

from app.core.settings import settings


def extract_id_from_url(url: str) -> int:
    match = re.search(r'/(\d+)/$', url)
    if match:
        return int(match.group(1))
    else:
        raise ValueError("Invalid URL format")


def pokemon_mapper(pokemon):
    return {
        "abilities": pokemon.abilities.split(","),
        "height": pokemon.height,
        "id": pokemon.id,
        "code": pokemon.code,
        "name": pokemon.name,
        "types": pokemon.types.split(","),
        "weight": pokemon.weight,
        "img": f"{settings.image_url}/{pokemon.id}.png"
    }


def pokemon_details_mapper(pokemon, stats):
    return {
        "abilities": pokemon.abilities.split(","),
        "height": pokemon.height,
        "id": pokemon.id,
        "code": pokemon.code,
        "name": pokemon.name,
        "stats": [
            {
                "value": stat.value,
                "name": stat.name
            }
            for stat in stats
        ],
        "types": pokemon.types.split(","),
        "weight": pokemon.weight,
        "img": f"{settings.image_url}/{pokemon.id}.png"
    }
