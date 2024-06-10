from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os
load_dotenv()


class Settings(BaseSettings):
    app_name: str = "Pokemon API"
    pokemon_api: str = "https://pokeapi.co/api/v2/pokemon"
    database_url: str = os.environ.get("DATABASE_URL")
    image_url: str = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/home/"

    class Config:
        env_file = ".env"


settings = Settings()
