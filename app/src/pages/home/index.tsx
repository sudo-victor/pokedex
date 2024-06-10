import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import LogoImg from "../../assets/logo.png"

import { AppDispatch, RootState } from "../../store/store";
import { fetchPokemons, setCurrentPage } from "../../store/pokemon-slice";
import { PokemonCard } from "../../components/cards/pokemon-card";
import { Pagination } from "../../components/pagination";

export function Home() {
  const dispatch = useDispatch<AppDispatch>();
  const { pokemons, pageCount, currentPage, status, error } = useSelector((state: RootState) => state.pokemon);
  
  useEffect(() => {
    dispatch(fetchPokemons(currentPage));
  }, [dispatch, currentPage]);

  const handlePageChange = (page: number) => {
    console.log(page)
    dispatch(setCurrentPage(page));
  };

  return (
    <div className="container mx-auto p-4">
      <img src={LogoImg} alt="Pokemon" width={200} className="m-auto mb-5" />
      {status === "loading" && <div className="text-center">Loading...</div>}
      {status === "failed" && <div className="text-center text-red-500">Algo de errado não está certo</div>}
      {status === "succeeded" && (
        <>
          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
            {pokemons.map((pokemon) => (
              <PokemonCard key={pokemon.name} pokemon={pokemon} />
            ))}
          </div>
          <Pagination
            pageCount={pageCount}
            currentPage={currentPage}
            onPageChange={handlePageChange} />
        </>
      )}
    </div>
  );
}
