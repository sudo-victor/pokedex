import { useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";

import PlaceholderImg from "../../assets/placeholder.png"
import { AppDispatch, RootState } from "../../store/store";
import { fetchPokemonDetails } from "../../store/pokemon-slice";
import typeColors from "../../utils/pokemon-colors";

export function PokemonDetail() {
  const { name } = useParams<{ name: string }>();
  const dispatch = useDispatch<AppDispatch>();
  const navigate = useNavigate();
  const { selectedPokemon, status, error } = useSelector(
    (state: RootState) => state.pokemon
  );

  useEffect(() => {
    if (name) {
      dispatch(fetchPokemonDetails(name));
    }
  }, [dispatch, name]);

  if (status === "loading") {
    return <div className="text-center">Loading...</div>;
  }

  if (status === "failed") {
    return <div className="text-center text-red-500">Error: {error}</div>;
  }

  if (!selectedPokemon) {
    return <div className="text-center">No Pokémon selected</div>;
  }

  return (
    <div className="container relative h-lvh flex items-center justify-center mx-auto">
      <button
        className="mb-4 px-4 py-2 bg-gray-500 text-white rounded absolute top-5 left-5"
        onClick={() => navigate(-1)}
      >
        Back
      </button>
      <div className="flex flex-col md:flex-row gap-8 rounded shadow-md bg-slate-50 p-4">
        <div className="flex-1">
          <img
            src={selectedPokemon.img}
            alt={selectedPokemon.name}
            className="w-full max-w-2xl h-auto"
            onError={(e) => {
              e.currentTarget.src = PlaceholderImg;
            }}
          />
          <div className="text-center mt-4 flex flex-col items-center justify-between gap-2">
            <div className="flex items-center gap-5">
              <h1 className="text-2xl font-bold capitalize">
                {selectedPokemon.name}
              </h1>
              <p>#{selectedPokemon.id}</p>
            </div>
            <div className="flex justify-center gap-2">
              {selectedPokemon.types.map((type: any) => (
                <span
                  key={type}
                  className="px-2 py-1 rounded text-slate-50"
                  style={{ backgroundColor: typeColors[type] }}
                >
                  {type}
                </span>
              ))}
            </div>
          </div>
        </div>
        <div className="flex-1 flex flex-col justify-between">
          <div>
            <div className="flex gap-5 items-center justify-between">
              <div className="mb-4">
                <h3 className="font-medium">height</h3>
                <p>{selectedPokemon.height} m</p>
              </div>
              <div className="mb-4">
                <h3 className="font-medium">weight</h3>
                <p>{selectedPokemon.weight} kg</p>
              </div>
            </div>
            <div className="mb-4">
              <h3 className="font-medium">abilities</h3>
              <div className="flex gap-2">
                {selectedPokemon.abilities.map((ability: string) => (
                  <span
                    key={ability}
                    className="px-2 py-1 rounded bg-slate-200 text-slate-700"
                  >
                    {ability}
                  </span>
                ))}
              </div>
            </div>
          </div>
          <div className="">
            <div className="flex flex-col gap-2">
              {selectedPokemon.stats.map((stat: any) => (
                <div key={stat.name}>
                  <div className="flex justify-between">
                    <span className="text-sm">{stat.name}</span>
                    <span>{stat.value}</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700">
                    <div
                      className="bg-blue-600 h-2.5 rounded-full"
                      style={{ width: `${(stat.value / 255) * 100}%` }}
                    ></div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
