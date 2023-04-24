import { Actor } from "./Actor";

export type FullCast = {
  imDbId: string;
  title: string;
  fullTitle: string;
  type: string;
  year: string;
  directors: FullCastDepartment;
  writers: FullCastDepartment;
  actors: Actor[];
  others: FullCastDepartment[];
  errorMessage: string;
};

export type FullCastItem = {
  id: string;
  name: string;
  description: string;
};

export type FullCastDepartment = {
  job: string;
  items: FullCastItem[];
};
