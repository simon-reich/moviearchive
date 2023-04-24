import type { RouteRecordRaw } from "vue-router";

export const archiveRoutes: Array<RouteRecordRaw> = [
  {
    path: "/archive",
    alias: ["/archive"],
    name: "archive",
    component: () => import("./Archive.vue"),
  },
];
