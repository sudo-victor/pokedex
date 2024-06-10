from app.database import engine, Base, database
from app.api.routes import router as pokemon_route
from app.usecases.fetch_pokemons_and_persist import fetch_pokemon_data
from app.core.settings import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*", "http://52.7.63.144", "https://52.7.63.144"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pokemon_route, prefix="/api/pokemons")


async def startup():
    await database.connect()
    Base.metadata.create_all(bind=engine)
    await fetch_pokemon_data()


async def shutdown():
    await database.disconnect()


app.add_event_handler("startup", startup)
app.add_event_handler("shutdown", shutdown)
