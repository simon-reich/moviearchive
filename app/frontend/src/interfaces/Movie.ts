import { Actor } from "@/types/Actor";
import { BoxOffice } from "@/types/BoxOffice";
import { DetailedThing } from "@/types/DetailedThing";
import { FullCast } from "@/types/FullCast";
import { Poster } from "@/types/Poster";
import { RatingList } from "@/types/RatingList";
import { Trailer } from "@/types/Trailer";
import { Image } from "@/types/Image";

export interface Movie {
  title: {
    key: string;
    value: string;
  };
  year: {
    key: string;
    value: number;
  };
  imdbID: {
    key: string;
    value: string;
  };
  originalTitle: {
    key: string;
    value: string;
  };
  medium: {
    key: string;
    value: string;
  };
  imageLink: {
    key: string;
    value: string;
  };
  releaseDate: {
    key: string;
    value: string;
  };
  runtime: {
    key: string;
    value: number;
  };
  plot: {
    key: string;
    value: string;
  };
  directorList: {
    key: string;
    value: DetailedThing[];
  };
  writerList: {
    key: string;
    value: DetailedThing[];
  };
  starList: {
    key: string;
    value: DetailedThing[];
  };
  actorList: {
    key: string;
    value: Actor[];
  };
  fullCast: {
    key: string;
    value: FullCast;
  };
  genreList: {
    key: string;
    value: string[];
  };
  countryList: {
    key: string;
    value: string[];
  };
  languageList: {
    key: string;
    value: string[];
  };
  contentRating: {
    key: string;
    value: string[];
  };
  keywordList: {
    key: string;
    value: string[];
  };
  companyList: {
    key: string;
    value: string[];
  };
  boxOffice: {
    key: string;
    value: BoxOffice;
  };
  imdbLink: {
    key: string;
    value: string;
  };
  imdbRating: {
    key: string;
    value: string;
  };
  imdbVotes: {
    key: string;
    value: string;
  };
  ratingList: {
    key: string;
    value: RatingList;
  };
  wikiLink: {
    key: string;
    value: string;
  };
  wikiTextShort: {
    key: string;
    value: string;
  };
  wikiTextShortHtml: {
    key: string;
    value: string;
  };
  wikiTextFull: {
    key: string;
    value: string;
  };
  wikiTextFullHtml: {
    key: string;
    value: string;
  };
  posterList: {
    key: string;
    value: Poster[];
  };
  imageList: {
    key: string;
    value: Image[];
  };
  trailer: {
    key: string;
    value: Trailer;
  };
  tvSeriesInfo?: {
    key: string;
    value: string | null;
  };
  tvEpisodeInfo?: {
    key: string;
    value: string | null;
  };
  personalRating?: {
    key: string;
    value: string | null;
  };
  personalNotes?: {
    key: string;
    value: string | null;
  };
}
