import { ApiService } from "../services/api/ApiService";
import { TmdbApiSearchResult } from "../interfaces/TmdbApiSearchResult";
import { defineStore } from "pinia";
import { IndexMovieDto } from "@/services/api/dtos/index-movie.dto";

export type ArchiveSearchStore = {
  searchResults: TmdbApiSearchResult[] | undefined;
};

const apiStore = {
  searchResults: [],
};

export const UseApiStore = defineStore("api", {
  state: (): ArchiveSearchStore => apiStore,

  actions: {
    async getSearchResults(query: string) {
      const response = await ApiService.searchMovie(query);
      if (response) {
        this.searchResults = response.data.results;
        return response.data.results;
      }
    },

    async indexMovie(dto: IndexMovieDto) {
      const response = await ApiService.indexMovie(dto);
      if (response && response.data === 201 && response.status === 200) {
        this.removeSearchResult(dto.tmdb_id);
      }
    },

    removeSearchResult(tmdbId: number) {
      this.searchResults = this.searchResults?.filter(
        (movie: TmdbApiSearchResult) => movie.id !== tmdbId
      );
    },
  },

  getters: {},
});
