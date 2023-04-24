import { SearchParameters } from "./SearchParameters";

export interface AdvancedQuery {
  parameters: SearchParameters;
  size: number;
}
