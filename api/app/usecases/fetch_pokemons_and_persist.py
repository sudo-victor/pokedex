import asyncio
import httpx
from sqlalchemy.orm import Session
from app.models.pokemon import Pokemon
from app.models.stat import Stat
from app.database import SessionLocal
from app.core.settings import settings

MAX_CONCURRENT_REQUESTS = 10


async def fetch_pokemon_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{settings.pokemon_api}?limit=10000")
        pokemon_list = response.json()

        total_pokemon_api = pokemon_list['count']

        db = SessionLocal()
        total_pokemon_db = db.query(Pokemon).count()
        db.close()

        if total_pokemon_api == total_pokemon_db:
            print("The database already has all the Pokémon.")
            return

        semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)
        tasks = [fetch_and_insert_pokemon_data(
            pokemon, client, semaphore) for pokemon in pokemon_list['results']]

        await asyncio.gather(*tasks)


async def fetch_and_insert_pokemon_data(pokemon, client, semaphore):
    async with semaphore:
        pokemon_response = await client.get(
            f"{settings.pokemon_api}/{pokemon['name']}"
        )
        pokemon_data = pokemon_response.json()

        db = SessionLocal()
        await insert_pokemon_data(db, pokemon_data)
        db.close()


async def insert_pokemon_data(db: Session, pokemon_data: dict):
    existing_pokemon = db.query(Pokemon).filter(
        Pokemon.name == pokemon_data["name"]).first()
    if existing_pokemon:
        return

    pokemon = Pokemon(
        code=str(pokemon_data["id"]),
        name=pokemon_data["name"],
        height=pokemon_data["height"],
        weight=pokemon_data["weight"],
        img=f"{settings.image_url}/{pokemon_data['id']}.png",
        types=",".join([t["type"]["name"] for t in pokemon_data["types"]]),
        abilities=",".join([a["ability"]["name"]
                           for a in pokemon_data["abilities"]])
    )
    db.add(pokemon)
    db.flush()

    for stat in pokemon_data["stats"]:
        db_stat = Stat(
            name=stat["stat"]["name"],
            value=stat["base_stat"],
            pokemon_id=pokemon.id
        )
        db.add(db_stat)

    db.commit()
