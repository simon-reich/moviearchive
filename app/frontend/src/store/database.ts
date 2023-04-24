import { defineStore } from "pinia";

export type DatabaseStore = {
  name: string;
  docs: number;
};

export const DatabaseBaseStore = defineStore("database", {
  state: (): DatabaseStore => ({
    name: "",
    docs: 0,
  }),

  actions: {},

  getters: {},
});
