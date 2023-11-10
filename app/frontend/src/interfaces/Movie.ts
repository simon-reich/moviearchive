import { CastMember } from "./CastMember";
import { CrewMember } from "./CrewMember";
import { Company } from "./Company";
import { Country } from "./Country";
import { Language } from "./Language";
import { Rating } from "./Rating";
import { Video } from "./Video";
import { Image } from "./Image";


export interface Movie {
    doc_id: string;
    
    backdrop_list: { 
        key: string, 
        value: Image[] | null 
    };
    boxoffice: {
        key: string, 
        value: number | null 
    };
    company_list: {
        key: string, 
        value: Company[] | null
    };
    content_rating: {
        key: string, value: string | null}; 
    country_list: {
        key: string, 
        value: Country[] | null
    };
    director_list: {
        key: string, 
        value: string[] | null
    };
    full_cast: {
        key: string, 
        value: CastMember[] | null
    };
    full_crew: {
        key: string, 
        value: CrewMember[] | null
    };
    genre_list: {
        key: string, 
        value: string[] | null
    };
    imdb_id: {
        key: string, 
        value: string | null
    };
    imdb_link: {
        key: string, 
        value: string | null
    };
    imdb_rating: {
        key: string, 
        value: number | null
    };
    imdb_votes: {
        key: string, 
        value: number | null
    };
    keyword_list: {
        key: string, 
        value: string[] | null
    };
    language_list: {
        key: string, 
        value: Language[] | null
    };
    main_cast: { 
        key: string, 
        value: string | null
    };
    original_title: {
        key: string, 
        value: string | null
    };
    personal_notes: {
        key: string, 
        value: string | null
    };
    personal_rating: {
        key: string, 
        value: number | null
    };
    poster: {
        key: string, 
        value: string | null
    };
    poster_list: {
        key: string, 
        value: Image[] | null
    };
    rating_list: {
        key: string, 
        value: Rating[] | null
    };
    release_date: {
        key: string, 
        value: string | null
    };
    runtime: {
        key: string, 
        value: number | null
    };
    synopsis: {
        key: string, 
        value: string | null
    };
    title: {
        key: string, 
        value: string | null
    };
    tmdb_id: {
        key: string, 
        value: number | null
    };
    trailer: {
        key: string, 
        value: string | null
    };
    video_list: {
        key: string, 
        value: Video[] | null
    };
    watched: {
        key: string, 
        value: boolean | null
    };
    writer_list: {
        key: string, 
        value: string[] | null
    };
    year: {
        key: string, 
        value: string | null
    };
}