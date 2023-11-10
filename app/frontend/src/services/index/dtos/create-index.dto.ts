import { Schemas } from "@/enums/Schemas";

export interface CreateIndexDto {
    name: string | null;
    schema: Schemas | null;
}