import { SearchParameters } from "./../interfaces/SearchParameters";
import { BasicQuery } from "../interfaces/BasicQuery";
import { DatabaseSearchResult } from "../interfaces/DatabaseSearchResult";
import { defineStore } from "pinia";
import { DatabaseService } from "@/services/database/DatabaseService";

export type SearchResultsStore = {
  searchResults: DatabaseSearchResult[] | undefined;
};

const defaultSearchResultsStore = {
  searchResults: [],
};

export const useSearchResultsStore = defineStore("searchResults", {
  state: (): SearchResultsStore => defaultSearchResultsStore,

  actions: {
    async getExactResults(query: BasicQuery) {
      this.searchResults = await DatabaseService.exactSearch(query);
    },

    async getMatchResults(query: BasicQuery) {
      this.searchResults = await DatabaseService.singleFieldSearch(query);
    },

    async getMultiMatchResults(query: BasicQuery) {
      this.searchResults = await DatabaseService.multiFieldSearch(query);
    },

    async getAdvancedSearchResults(parameters: SearchParameters) {
      this.searchResults = await DatabaseService.advancedSearch(parameters);
    },
  },

  getters: {},
});
