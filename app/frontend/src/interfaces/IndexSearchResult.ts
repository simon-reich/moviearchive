import { Highlight } from "./Highlight";

export interface IndexSearchResult {
  score?: number;
  doc_id: string;
  imdb_id: string;
  title: string;
  year: number;
  genre: string[];
  runtime: number;
  director: string[];
  stars: string[];
  language: string[];
  country: string[];
  image: string;
  highlight?: Highlight[];
}
