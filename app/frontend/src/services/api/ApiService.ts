import axios from "axios";
import { IndexMovieDto } from "./dtos/index-movie.dto";
import { IndexByFileDto } from "./dtos/index-by-file.dto";

export const ApiService = {
  searchMovie: async (query: string) => {
    const url = `${import.meta.env.VITE_BACKEND_URL}api/search`;
    const dto = {
      title: query,
    };
    try {
      const response = await axios.post(url, dto);
      return response;
    } catch (err) {
      console.log(err);
    }
  },

  indexMovie: async (dto: IndexMovieDto) => {
    const url = `${import.meta.env.VITE_BACKEND_URL}api/index`;
    try {
      const response = await axios.post(url, dto);
      return response;
    } catch (err) {
      console.log(err);
    }
  },

  indexByFile: async (dto: IndexByFileDto) => {
    const url = `${import.meta.env.VITE_BACKEND_URL}api/index-by-file`;
    try {
      const response = await axios.post(url, dto);
      return response;
    } catch (err) {
      console.log(err);
    }
  },
};
