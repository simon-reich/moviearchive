import { SearchParameters } from "../interfaces/SearchParameters";
import { BasicQuery } from "../interfaces/BasicQuery";
import { IndexSearchResult } from "../interfaces/IndexSearchResult";
import { defineStore } from "pinia";
import { IndexService } from "@/services/index/IndexService";
import { AdvancedQuery } from "@/interfaces/AdvancedQuery";

export type IndexSearchStore = {
  query: BasicQuery | AdvancedQuery | null;
  searchResults: IndexSearchResult[] | undefined;
};

const defaultIndexSearchStore = {
  query: null,
  searchResults: [],
};

export const UseIndexSearchStore = defineStore("indexSearch", {
  state: (): IndexSearchStore => defaultIndexSearchStore,

  actions: {
    async getExactResults(query: BasicQuery) {
      this.searchResults = await IndexService.exactSearch(query);
    },

    async getMatchResults(query: BasicQuery) {
      this.searchResults = await IndexService.singleFieldSearch(query);
    },

    async getMultiMatchResults(query: BasicQuery) {
      this.searchResults = await IndexService.multiFieldSearch(query);
    },

    async getAdvancedSearchResults(parameters: SearchParameters) {
      this.searchResults = await IndexService.advancedSearch(parameters);
    },

    async getMovieByImdbId(imdbId: string) {
      return await IndexService.getByImdbId(imdbId);
    },

    deleteDocByImdbId(docId: string) {
      this.searchResults = this.searchResults?.filter((searchResult) => searchResult.doc_id != docId) 
    }
  },

  getters: {},
});
