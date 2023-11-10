import axios from "axios";
import { CreateIndexDto } from "../index/dtos/create-index.dto";

export const DatabaseService = {
  getIndexByName: async (name: string) => {
    const url = `${import.meta.env.VITE_BACKEND_URL}db/index/${name}`;
    try {
      const response = await axios.get(url);
      return response;
    } catch (err) {
      console.log(err);
    }
  },

  getAllIndices: async () => {
    const url = `${import.meta.env.VITE_BACKEND_URL}db/index`;
    try {
      const response = await axios.get(url);
      return response;
    } catch (err) {
      console.log(err);
    }
  },


  createIndex: async (dto: CreateIndexDto) => {
    const url = `${import.meta.env.VITE_BACKEND_URL}db/index`;
    try {
      const response = await axios.post(url, dto);
      return response;
    } catch (err) {
      console.log(err);
    }
  },

  deleteIndexById: async (id: number) => {
    const url = `${import.meta.env.VITE_BACKEND_URL}db/index/${id}`;
    try {
      const response = await axios.delete(url);
      return response;
    } catch (err) {
      console.log(err);
    }
  },

  deleteIndexByName: async (name: string) => {
    const url = `${import.meta.env.VITE_BACKEND_URL}db/index/${name}`;
    try {
      const response = await axios.delete(url);
      return response;
    } catch (err) {
      console.log(err);
    }
  },



};
