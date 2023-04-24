import { SearchParameters } from './../../interfaces/SearchParameters';
import { BasicQuery } from "@/interfaces/BasicQuery";
import { DatabaseSearchResult } from "@/interfaces/DatabaseSearchResult";
import axios from "axios";
import { AdvancedQuery } from '@/interfaces/AdvancedQuery';
import { IndexFolderDto } from './dtos/index-folder.dto';

export const DatabaseService = {
  createIndex: async () => {
    const url = `${import.meta.env.VITE_BACKEND_URL}es/create`;
    console.log(url)
    try {
      const response = await axios.get(url);
      return response;
    } catch (err) {
      console.log(err);
    }
  },

  getAllIndicies: async () => {
    const url = `${import.meta.env.VITE_BACKEND_URL}es/all`;
    try {
      const response = await axios.get(url);
      return response;
    } catch (err) {
      console.log(err);
    }
  },

  indexFolder: async () => {
    const url = `${import.meta.env.VITE_BACKEND_URL}es/index-folder`;
    try {
      const response = await axios.get(url);
      return response;
    } catch (err) {
      console.log(err);
    }
  },

  exactSearch: async (dto: BasicQuery) => {
    const url = `${import.meta.env.VITE_BACKEND_URL}es/search/exact`;
    try {
      const response = await axios.post(url, dto);
      const movies: DatabaseSearchResult[] = response.data.map((data: any) => {
        return {
          id: data._source.imdbID,
          title: data._source.title,
          year: parseInt(data._source.year),
          genre: data._source.genreList,
          runtime: parseInt(data._source.runtime),
          director: data._source.directorList.map((obj: any) => obj.name),
          stars: data._source.starList.map((obj: any) => obj.name),
          language: data._source.languageList,
          country: data._source.countryList,
          image: data._source.imageLink,
        };
      });
      return movies;
    } catch (err) {
      console.log(err);
    }
  },

  singleFieldSearch: async (dto: BasicQuery) => {
    const url = `${import.meta.env.VITE_BACKEND_URL}es/search/single`;
    try {
      const response = await axios.post(url, dto);
      const movies: DatabaseSearchResult[] = response.data.map((data: any) => {
        return {
          id: data._source.imdbID,
          title: data._source.title,
          year: parseInt(data._source.year),
          genre: data._source.genreList,
          runtime: parseInt(data._source.runtime),
          director: data._source.directorList.map((obj: any) => obj.name),
          stars: data._source.starList.map((obj: any) => obj.name),
          language: data._source.languageList,
          country: data._source.countryList,
          image: data._source.imageLink,
        };
      });
      return movies;
    } catch (err) {
      console.log(err);
    }
  },

  multiFieldSearch: async (dto: BasicQuery) => {
    const url = `${import.meta.env.VITE_BACKEND_URL}es/search/multi`;
    try {
      const response = await axios.post(url, dto);
      const movies: DatabaseSearchResult[] = response.data.map((data: any) => {
        return {
          id: data._source.imdbID,
          title: data._source.title,
          year: parseInt(data._source.year),
          genre: data._source.genreList,
          runtime: parseInt(data._source.runtime),
          director: data._source.directorList.map((obj: any) => obj.name),
          stars: data._source.starList.map((obj: any) => obj.name),
          language: data._source.languageList,
          country: data._source.countryList,
          image: data._source.imageLink,
        };
      });
      return movies;
    } catch (err) {
      console.log(err);
    }
  },

  getById: async (imdbId: string) => {
    const url = `${import.meta.env.VITE_BACKEND_URL}es/search/id/${imdbId}`;
    try {
      const response = await axios.get(url);
      return response.data;
    } catch (err) {
      console.log(err);
    }
  },

  getDistinctValues: async (field: string) => {
    const url = `${import.meta.env.VITE_BACKEND_URL}es/search/values/${field}`;
    try {
      const response = await axios.get(url);
      return response.data;
    } catch (err) {
      console.log(err);
    }
  },

  advancedSearch: async (parameters: SearchParameters) => {
    const url = `${import.meta.env.VITE_BACKEND_URL}es/search/advanced`;
    const dto: AdvancedQuery = {
      parameters: parameters,
      size: 1000,
    }
    try {
      const response = await axios.post(url, dto);
      return response.data;
    } catch (err) {
      console.log(err);
    }
  },
};
