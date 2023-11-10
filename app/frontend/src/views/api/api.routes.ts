import type { RouteRecordRaw } from "vue-router";

export const apiRoutes: Array<RouteRecordRaw> = [
  {
    path: "/api",
    alias: ["/api"],
    name: "api",
    component: () => import("./Api.vue"),
  },
];
