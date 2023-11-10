import { SearchParameters } from '../../interfaces/SearchParameters';
import { BasicQuery } from "@/interfaces/BasicQuery";
import { IndexSearchResult } from "@/interfaces/IndexSearchResult";
import axios from "axios";
import { AdvancedQuery } from '@/interfaces/AdvancedQuery';
import { MovieEditableFields } from '@/interfaces/MovieEditableFields';
import { CreateIndexDto } from './dtos/create-index.dto';
import { Index } from '@/interfaces/Index';
import { EditIndexDto } from './dtos/edit-index.dto';
import { UseIndexStore } from '@/store/IndexStore';
import { IndexFolderDto } from './dtos/index-folder.dto';

export const IndexService = {
  createIndex: async (dto: CreateIndexDto) => {
    const url = `${import.meta.env.VITE_BACKEND_URL}es/index/create`;
    try {
      const response = await axios.post(url, dto);
      return response;
    } catch (err) {
      console.log(err);
    }
  },


  editIndex: async (dto: EditIndexDto) => {
    const url = `${import.meta.env.VITE_BACKEND_URL}es/index/edit`;
    try {
      const response = await axios.put(url, dto);
      return response;
    } catch (err) {
      console.log(err);
    }
  },


  deleteIndex: async (indexName: string) => {
    const url = `${import.meta.env.VITE_BACKEND_URL}es/index/delete/${indexName}`;
    try {
      const response = await axios.delete(url);
      return response;
    } catch (err) {
      console.log(err);
    }
  },


  getAllIndices: async () => {
    const url = `${import.meta.env.VITE_BACKEND_URL}es/all`;
    try {
      const response = await axios.get(url);
      const indices: Index[] = response.data.map((data: any) => {
        return {
          uuid: data.uuid,
          index: data.index,
          docs_count: data['docs.count'],
          docs_deleted: data['docs.deleted'],
          health: data.health,
          store_size: data['store.size']
        }
      });
      return indices;
    } catch (err) {
      console.log(err);
    }
  },


  getIndex: async (indexName: string) => {
    const url = `${import.meta.env.VITE_BACKEND_URL}es/${indexName}`;
    try {
      const response = await axios.get(url);
      const index: Index[] = response.data.map((data: any) => {
        return {
          uuid: data.uuid,
          index: data.index,
          docs_count: data['docs.count'],
          docs_deleted: data['docs.deleted'],
          health: data.health,
          store_size: data['store.size']
        }
      });
      return index[0];
    } catch (err) {
      console.log(err);
    }
  },


  exactSearch: async (dto: BasicQuery) => {
    const indexName = await UseIndexStore().getSelectedOrDefault();
    const url = `${import.meta.env.VITE_BACKEND_URL}es/search/exact/${indexName}`;
    try {
      const response = await axios.post(url, dto);
      const movies: IndexSearchResult[] = response.data.map((data: any) => {
        return {
          doc_id: data._id,
          imdb_id: data._source.imdb_id,
          title: data._source.title,
          year: parseInt(data._source.year),
          genre: data._source.genre_list,
          runtime: parseInt(data._source.runtime),
          director: data._source.director_list,
          stars: data._source.main_cast,
          language: data._source.language_list.map((obj: any) => obj.english_name),
          country: data._source.country_list.map((obj: any) => obj.name),
          image: data._source.poster,
        };
      });
      return movies;
    } catch (err) {
      console.log(err);
    }
  },


  singleFieldSearch: async (dto: BasicQuery) => {
    const indexName = await UseIndexStore().getSelectedOrDefault();
    const url = `${import.meta.env.VITE_BACKEND_URL}es/search/single-field/${indexName}`;
    try {
      const response = await axios.post(url, dto);
      const movies: IndexSearchResult[] = response.data.map((data: any) => {
        return {
          doc_id: data._id,
          imdb_id: data._source.imdb_id,
          title: data._source.title,
          year: parseInt(data._source.year),
          genre: data._source.genre_list,
          runtime: parseInt(data._source.runtime),
          director: data._source.director_list,
          stars: data._source.main_cast,
          language: data._source.language_list.map((obj: any) => obj.name),
          country: data._source.country_list.map((obj: any) => obj.name),
          image: data._source.poster,
        };
      });
      return movies;
    } catch (err) {
      console.log(err);
    }
  },


  multiFieldSearch: async (dto: BasicQuery) => {
    const indexName = await UseIndexStore().getSelectedOrDefault();
    const url = `${import.meta.env.VITE_BACKEND_URL}es/search/multi-field/${indexName}`;
    console.log(url);    
    try {
      const response = await axios.post(url, dto);
      const movies: IndexSearchResult[] = response.data.map((data: any) => {
        return {
          doc_id: data._id,
          imdb_id: data._source.imdb_id,
          title: data._source.title,
          year: parseInt(data._source.year),
          genre: data._source.genre_list,
          runtime: parseInt(data._source.runtime),
          director: data._source.director_list,
          stars: data._source.main_cast,
          language: data._source.language_list.map((obj: any) => obj.name),
          country: data._source.country_list.map((obj: any) => obj.name),
          image: data._source.poster,
        };
      });
      return movies;
    } catch (err) {
      console.log(err);
    }
  },


  advancedSearch: async (parameters: SearchParameters) => {
    const indexName = await UseIndexStore().getSelectedOrDefault();
    const url = `${import.meta.env.VITE_BACKEND_URL}es/search/advanced/${indexName}`;
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


  getByImdbId: async (imdbId: string) => {
    const indexName = await UseIndexStore().getSelectedOrDefault();
    const url = `${import.meta.env.VITE_BACKEND_URL}es/search/id/${indexName}/${imdbId}`;
    try {
      const response = await axios.get(url);
      return response.data;
    } catch (err) {
      console.log(err);
    }
  },


  getDistinctValues: async (field: string) => {
    const indexName = await UseIndexStore().getSelectedOrDefault();
    const url = `${import.meta.env.VITE_BACKEND_URL}es/search/values/${indexName}/${field}`;
    try {
      const response = await axios.get(url);
      return response.data;
    } catch (err) {
      console.log(err);
    }
  },


  getEditableMovieValues: async (imdbId: string) => {
    const indexName = await UseIndexStore().getSelectedOrDefault();
    const url = `${import.meta.env.VITE_BACKEND_URL}es/edit/id/${indexName}/${imdbId}`;
    try {
      const response = await axios.get(url);
      const editableValues: MovieEditableFields[] = response.data.map((data: any) => {
        return {
          doc_id: data._id,
          imdb_id: data._source.imdb_id,
          watched: data._source.watched,
          personal_notes: data._source.personal_notes,
          personal_rating: data._source.personal_rating,
        };
      });
      return editableValues;
    } catch (err) {
      console.log(err);
    }
  },


  editMovie: async (dto: MovieEditableFields) => {
    const indexName = await UseIndexStore().getSelectedOrDefault();
    const url = `${import.meta.env.VITE_BACKEND_URL}es/edit/${indexName}`;
    try {
      const response = await axios.post(url, dto);
      return response
    } catch (err) {
      console.log(err);
    }
  },


  deleteMovieByImdbId: async (imdbId: string) => {
    const indexName = await UseIndexStore().getSelectedOrDefault();
    const url = `${import.meta.env.VITE_BACKEND_URL}es/delete/id/${indexName}/${imdbId}`;
    try {
      const response = await axios.delete(url);
      return response;
    } catch (err) {
      console.log(err);
    }
  },


  deleteMovieByDocId: async (docId: string) => {
    const indexName = await UseIndexStore().getSelectedOrDefault();
    const url = `${import.meta.env.VITE_BACKEND_URL}es/delete/${indexName}/doc-id/${docId}`;
    try {
      const response = await axios.delete(url);
      return response;
    } catch (err) {
      console.log(err);
    }
  },


  indexFolder: async (dto: IndexFolderDto) => {
    const indexName = await UseIndexStore().getSelectedOrDefault();
    const url = `${import.meta.env.VITE_BACKEND_URL}es/indexing/${indexName}/index-folder`;
    try {
      const response = await axios.post(url, dto);
      return response;
    } catch (err) {
      console.log(err);
    }
  },

};
