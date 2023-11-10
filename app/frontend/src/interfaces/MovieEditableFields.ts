export interface MovieEditableFields {
    doc_id: string;
    imdb_id: string;
    watched: boolean | null;
    personal_notes: string | null;
    personal_rating: number | null;
}