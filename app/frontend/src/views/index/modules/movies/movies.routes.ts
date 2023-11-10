import type { RouteRecordRaw } from "vue-router";

export const moviesRoutes: Array<RouteRecordRaw> = [
  {
    path: "movies/:imdbId",
    name: "index.movies",
    props: true,
    component: () => import("./components/DisplayMovie.vue"),
    children: [],
  },
];
