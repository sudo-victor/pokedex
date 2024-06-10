import { useState } from "react";
import { Link } from "react-router-dom";
import { Pokemon } from "../../../models/pokemon";

import PlaceholderImg from "../../../assets/placeholder.png";

interface PokemonCardProps {
  pokemon: Pokemon;
}

export function PokemonCard({ pokemon }: PokemonCardProps) {
  const [imgSrc, setImgSrc] = useState<string>(PlaceholderImg);

  return (
    <Link
      to={`/pokemon/${pokemon.name}`}
      className="border p-4 rounded shadow-md bg-white flex flex-col gap-3"
    >
      <img
        src={imgSrc}
        alt={pokemon.name}
        className="w-[60%] self-center rounded-md"
        onLoad={() => {
          setImgSrc(pokemon.img);
        }}
        onError={(e) => {
          e.currentTarget.src = PlaceholderImg;
        }}
      />
      <h3 className="text-lg font-bold capitalize">{pokemon.name}</h3>
    </Link>
  );
}
