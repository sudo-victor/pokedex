import { createSlice, createAsyncThunk, PayloadAction } from "@reduxjs/toolkit";
import axios from "axios";
import { Pokemon } from "../models/pokemon";
import { PokemonDetail } from "../models/pokemon-detail";
import { env } from "../config/env";

interface PokemonState {
  pokemons: Pokemon[];
  selectedPokemon: PokemonDetail | null;
  pageCount: number;
  currentPage: number;
  status: "idle" | "loading" | "succeeded" | "failed";
  error: string | null;
}

const initialState: PokemonState = {
  pokemons: [],
  selectedPokemon: null,
  pageCount: 0,
  currentPage: 0,
  status: "idle",
  error: null,
};

const API_URL = env.api_url

export const fetchPokemons = createAsyncThunk(
  "pokemon/fetchPokemons",
  async (page: number, { rejectWithValue }) => {
    try {
      const limit = 8;
      const response = await axios.get(
        `${API_URL}/pokemons?limit=${limit}&page=${
          page <= 0 ? 1 : page
        }`
      );
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

export const fetchPokemonDetails = createAsyncThunk(
  "pokemon/fetchPokemonDetails",
  async (name: string, { rejectWithValue }) => {
    try {
      const response = await axios.get(
        `${API_URL}/pokemons/${name}`
      );
      return response.data;
    } catch (error) {
      return rejectWithValue(error.response.data);
    }
  }
);

const pokemonSlice = createSlice({
  name: "pokemon",
  initialState,
  reducers: {
    setCurrentPage: (state, action: PayloadAction<number>) => {
      state.currentPage = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchPokemons.pending, (state) => {
        state.status = "loading";
        state.error = null;
      })
      .addCase(fetchPokemons.fulfilled, (state, action) => {
        state.status = "succeeded";
        state.pokemons = action.payload.result;
        state.pageCount = Math.ceil(action.payload.count / 8);
      })
      .addCase(fetchPokemons.rejected, (state, action) => {
        state.status = "failed";
        state.error = action.payload as string;
      })
      .addCase(fetchPokemonDetails.pending, (state) => {
        state.status = "loading";
        state.error = null;
      })
      .addCase(fetchPokemonDetails.fulfilled, (state, action) => {
        state.status = "succeeded";
        state.selectedPokemon = action.payload.result;
      })
      .addCase(fetchPokemonDetails.rejected, (state, action) => {
        state.status = "failed";
        state.error = action.payload as string;
      });
  },
});

export const { setCurrentPage } = pokemonSlice.actions;

export default pokemonSlice.reducer;
