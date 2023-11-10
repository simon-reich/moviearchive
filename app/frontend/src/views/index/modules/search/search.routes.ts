import type { RouteRecordRaw } from "vue-router";

export const searchRoutes: Array<RouteRecordRaw> = [
  {
    path: "search",
    name: "index.search",
    component: () => import("./Search.vue"),
    children: [],
  },
];
