import { moviesRoutes } from './modules/movies/movies.routes';
import type { RouteRecordRaw } from "vue-router";
import { searchRoutes } from "./modules/search/search.routes";

export const indexRoutes: Array<RouteRecordRaw> = [
  {
    path: "/index",
    alias: ["/index"],
    name: "index",
    redirect: { name: "index.search" },
    component: () => import("./Index.vue"),
    children: [...searchRoutes, ...moviesRoutes],
  },
];
