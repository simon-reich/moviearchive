import { router } from "./routes";

import i18n from "./plugins/i18n";

import { createApp } from "vue";
import { createPinia } from "pinia";
import { createHead } from "@vueuse/head";

import App from "./App.vue";

const app = createApp(App);
const pinia = createPinia();
const head = createHead();

import './assets/css/main.css';

import "virtual:windi-base.css";
import "virtual:windi-components.css";
import "virtual:windi-utilities.css";
import "virtual:windi-devtools";

import "@iconify/iconify";
import "@purge-icons/generated";

app.use(router);
app.use(pinia);
app.use(head);
app.use(i18n);

app.mount("#app");
