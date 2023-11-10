export interface CrewMember {
    adult: boolean | null;
    credit_id: string | null;
    department: string;
    gender: number | null;
    id: number;
    job: string;
    known_for_department: string | null;
    name: string;
    original_name: string | null;
    popularity: number | null;
    profile_path: string | null;
}