from fastapi import HTTPException
from app.repositories.pokemon_repository import get_pokemon_details_from_db


async def fetch_pokemon_detail(name_or_code: int | str):
    print(name_or_code)
    pokemon_details = get_pokemon_details_from_db(name_or_code)
    if not pokemon_details:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    return {"result": pokemon_details}
