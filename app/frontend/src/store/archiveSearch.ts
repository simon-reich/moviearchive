import { ImdbApiService } from "./../services/imdbApi/ImdbApiService";
import { ImdbApiSearchResult } from "./../interfaces/ImdbApiSearchResult";
import { defineStore } from "pinia";

export type ArchiveSearchStore = {
  searchResults: ImdbApiSearchResult[] | undefined;
};

const archiveSearchStore = {
  searchResults: [],
};

export const UseArchiveSearchStore = defineStore("archiveSearch", {
  state: (): ArchiveSearchStore => archiveSearchStore,

  actions: {
    async getSearchResults(query: string) {
      const response = await ImdbApiService.searchMovie(query);
      if (response) {
        this.searchResults = response.data.results;
        return response.data.results;
      }
    },

    removeMovie(imdbId: string) {
      this.searchResults = this.searchResults?.filter(
        (movie: ImdbApiSearchResult) => movie.id !== imdbId
      );
    },
  },

  getters: {},
});
