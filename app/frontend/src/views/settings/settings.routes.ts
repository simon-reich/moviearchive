import type { RouteRecordRaw } from "vue-router";

export const settingsRoutes: Array<RouteRecordRaw> = [
  {
    path: "/settings",
    alias: ["/settings"],
    name: "settings",
    component: () => import("./Settings.vue"),
  },
];