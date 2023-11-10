import axios from "axios";
import { IndexMovieDto } from "./dtos/index-movie.dto";

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
};
