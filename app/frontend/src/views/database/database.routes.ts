import { moviesRoutes } from './modules/movies/movies.routes';
import type { RouteRecordRaw } from "vue-router";
import { searchRoutes } from "./modules/search/search.routes";

export const databaseRoutes: Array<RouteRecordRaw> = [
  {
    path: "/database",
    alias: ["/database"],
    name: "database",
    redirect: { name: "database.search" },
    component: () => import("./Database.vue"),
    children: [...searchRoutes, ...moviesRoutes],
  },
];
