import axios from "axios";

export const ImdbApiService = {
  searchMovie: async (query: string) => {
    const url = `${import.meta.env.VITE_BACKEND_URL}imdbapi/search`;
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

  archiveMovie: async (imdbId: string) => {
    const url = `${import.meta.env.VITE_BACKEND_URL}imdbapi/${imdbId}`;
    try {
      const response = await axios.get(url);
      return response;
    } catch (err) {
      console.log(err);
    }
  },
};
