from fastapi import APIRouter, Query, Path

from app.usecases.fetch_pokemons import fetch_pokemons
from app.usecases.fetch_pokemon_detail import fetch_pokemon_detail

router = APIRouter()


@router.get("/")
async def list_pokemons_route(
    page: int = Query(
        default=1,
        description="Current list page of pokemons"
    ),
    limit: int = Query(
        default=100,
        description="Total number of pokemons to fetch"
    ),
):
    return await fetch_pokemons(page, limit)


@router.get("/{name_or_code}")
async def pokemon_detail_route(
    name_or_code: str | int = Path(description="Name or code of pokemon")
):
    return await fetch_pokemon_detail(name_or_code)
