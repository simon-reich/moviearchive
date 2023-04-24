import type { RouteRecordRaw } from "vue-router";

export const moviesRoutes: Array<RouteRecordRaw> = [
  {
    path: "movies/:id",
    name: "database.movies",
    props: true,
    component: () => import("./modules/movie/Movie.vue"),
    children: [],
  },
];
