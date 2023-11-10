import { apiRoutes } from "./views/api/api.routes";
import { indexRoutes } from "./views/index/index.routes";
import { settingsRoutes } from "./views/settings/settings.routes";
import { homeRoutes } from "./views/home/home.routes";
import type { RouteRecordRaw } from "vue-router";
import { createRouter, createWebHistory } from "vue-router";

const routes: Array<RouteRecordRaw> = [
  ...homeRoutes,
  ...indexRoutes,
  ...apiRoutes,
  ...settingsRoutes,
];

export const router = createRouter({
  history: createWebHistory(),
  routes: [...routes],
});
