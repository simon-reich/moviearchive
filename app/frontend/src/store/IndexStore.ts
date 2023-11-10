import { Index } from "@/interfaces/Index";
import { MovieEditableFields } from "@/interfaces/MovieEditableFields";
import { IndexService } from "@/services/index/IndexService";
import { CreateIndexDto } from "@/services/index/dtos/create-index.dto";
import { EditIndexDto } from "@/services/index/dtos/edit-index.dto";
import { IndexFolderDto } from "@/services/index/dtos/index-folder.dto";
import { defineStore } from "pinia";

export type IndexStore = {
  indices: Index[] | undefined;
  selected: Index | undefined;
};

export const UseIndexStore = defineStore("index", {
  state: (): IndexStore => ({
    indices: [],
    selected: undefined,
  }),

  actions: {
    async initialize() {
      await this.getIndicies();
      if (this.indices && !this.selected) {
        this.selected = this.indices[0];
      }
    },

    async getIndicies() {
      this.indices = await IndexService.getAllIndices();
    },

    async createIndex(dto: CreateIndexDto) {
      const response = await IndexService.createIndex(dto);
      this.getIndicies();
      return response;
    },

    async editIndex(dto: EditIndexDto) {
      const response = await IndexService.editIndex(dto);
      return response;
    },

    async deleteIndex(indexName: string) {
      const response = await IndexService.deleteIndex(indexName);
      this.getIndicies();
      return response;
    },

    async getEditableMovieValues(imdbId: string) {
      const response = await IndexService.getEditableMovieValues(imdbId)
      return response;
    },

    async editMovie(dto: MovieEditableFields) {
      const response = await IndexService.editMovie(dto);
      return response;
    },

    async deleteMovie(docId: string) {
      const response = await IndexService.deleteMovieByDocId(docId);
      return response;
    },

    async selectIndex(indexName: string) {
      this.selected = await IndexService.getIndex(indexName);
    },

    async getSelectedOrDefault() {
      if (!this.selected) {
        await this.initialize();
      }
      return this.selected ? this.selected.index : null;
    },

    async indexFolder(dto: IndexFolderDto) {
      const response = await IndexService.indexFolder(dto);
      return response; 
    }
  },

  getters: {},
});
