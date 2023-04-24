import type { RouteRecordRaw } from "vue-router";

export const homeRoutes: Array<RouteRecordRaw> = [
  {
    path: "/",
    alias: ["/home"],
    name: "home",
    component: () => import("./Home.vue"),
  },
];
