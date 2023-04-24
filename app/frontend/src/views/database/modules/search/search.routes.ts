import type { RouteRecordRaw } from "vue-router";

export const searchRoutes: Array<RouteRecordRaw> = [
  {
    path: "search",
    name: "database.search",
    component: () => import("./Search.vue"),
    children: [],
  },
];
