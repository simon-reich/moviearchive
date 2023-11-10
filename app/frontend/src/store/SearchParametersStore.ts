import { SearchParameters } from "../interfaces/SearchParameters";

export type SearchParametersStore = {
  parameters: SearchParameters;
};

const defaultSearchParametersStore = {
  parameters: {
    year: null,
    genres: [],
    runtime: null,
    content: "",
    director: "",
    actors: [],
    staff: "",
    country: "",
    language: "",
  },
};

export const useSearchParametersStore = defineStore("searchParameters", {
  state: (): SearchParametersStore => defaultSearchParametersStore,

  actions: {},

  getters: {},
});
