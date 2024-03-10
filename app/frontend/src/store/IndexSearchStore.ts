import { SearchParameters } from "../interfaces/SearchParameters";
import { BasicQuery } from "../interfaces/BasicQuery";
import { IndexSearchResult } from "../interfaces/IndexSearchResult";
import { defineStore } from "pinia";
import { IndexService } from "@/services/index/IndexService";
import { AdvancedQuery } from "@/interfaces/AdvancedQuery";
import { HighlightAggregation } from "@/interfaces/HighlightAggregation";

export type IndexSearchStore = {
  query: BasicQuery | AdvancedQuery | null;
  searchResults: IndexSearchResult[] | undefined;
  highlightAggregation: HighlightAggregation[];
};

const defaultIndexSearchStore = {
  query: null,
  searchResults: [],
  highlightAggregation: [],
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
      this.searchResults?.sort((a, b) => {
        if (a.score === undefined && b.score === undefined) return 0;
        if (a.score === undefined) return 1;
        if (b.score === undefined) return -1;
        return b.score - a.score;
      });
      this.aggregateHighlights();
    },

    async getAdvancedSearchResults(parameters: SearchParameters) {
      this.searchResults = await IndexService.advancedSearch(parameters);
    },

    async getMovieByImdbId(imdbId: string) {
      return await IndexService.getByImdbId(imdbId);
    },

    aggregateHighlights() {
      const allHighlightFields: string[] = [];
      const aggregationMap: Record<string, string[]> = {};
      
      // get all unique highlight fields
      this.searchResults?.forEach(result => {
        if (result.highlight) {
          result.highlight.forEach(highlight => {
            if (!allHighlightFields.includes(highlight.field)) {
              allHighlightFields.push(highlight.field);
            }
          });
        }
      });
      // map all movie titles with highlight values in a highlight field to that highlight field
      this.searchResults?.forEach(result => {
        allHighlightFields.forEach(field => {
          if (result.highlight && result.highlight.some(h => h.field === field && h.values.length > 0)) {
            if (!aggregationMap[field]) {
              aggregationMap[field] = [];
            }
            aggregationMap[field].push(result.title);
          }
        });
      });
      // fill highlightAggregation with the computed results
      this.highlightAggregation = Object.entries(aggregationMap).map(([field, values]) => ({
        field,
        asText: `Aggregated titles for ${field}`,
        values: [...new Set(values)],
      }));
    },

    deleteDocByImdbId(docId: string) {
      this.searchResults = this.searchResults?.filter((searchResult) => searchResult.doc_id != docId) 
    }
  },

  getters: {},
});
