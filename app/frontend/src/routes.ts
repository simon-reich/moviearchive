import { archiveRoutes } from "./views/archive/archive.routes";
import { databaseRoutes } from "./views/database/database.routes";
import { settingsRoutes } from "./views/settings/settings.routes";
import { homeRoutes } from "./views/home/home.routes";
import type { RouteRecordRaw } from "vue-router";
import { createRouter, createWebHistory } from "vue-router";

const routes: Array<RouteRecordRaw> = [
  ...homeRoutes,
  ...databaseRoutes,
  ...archiveRoutes,
  ...settingsRoutes,
];

export const router = createRouter({
  history: createWebHistory(),
  routes: [...routes],
});
