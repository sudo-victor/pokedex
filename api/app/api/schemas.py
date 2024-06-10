from pydantic import BaseModel
from typing import List, Optional


class PokemonAbility(BaseModel):
    name: str


class PokemonType(BaseModel):
    name: str


class PokemonStat(BaseModel):
    value: int
    name: str


class PokemonDetail(BaseModel):
    id: int
    code: str
    name: str
    height: int
    weight: int
    abilities: List[str]
    types: List[str]
    stats: Optional[List[PokemonStat]]
    img: str


class PokemonListItem(BaseModel):
    id: int
    code: str
    name: str
    height: int
    weight: int
    abilities: List[str]
    types: List[str]
    img: str


class PokemonListResponse(BaseModel):
    count: int
    result: List[PokemonListItem]
    current_page: int
    limit: int
    total_pages: int


class PokemonDetailResponse(BaseModel):
    result: PokemonDetail
