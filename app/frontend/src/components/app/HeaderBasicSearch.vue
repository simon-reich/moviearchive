<script setup lang="ts">
import { BasicQuery } from "@/interfaces/BasicQuery";
import { router } from "@/routes";
import { UseIndexSearchStore } from "@/store/IndexSearchStore";

const indexSearchStore = UseIndexSearchStore();

const query = ref<BasicQuery>({
  field: import.meta.env.VITE_QUERY_FIELD,
  value: "",
  size: import.meta.env.VITE_DB_DATA_ARRAY_SIZE,
});

const searchMovie = async () => {
  await indexSearchStore.getMultiMatchResults(query.value);
  router.push({ name: "index.search" });
};
</script>

<template>
  <header class="sticky h-18 w-full bg-dark-800 text-white py-1">
    <div
      class="h-full flex justify-between items-center container mx-auto gap-2"
    >
      <div class="m-5">
        <router-link :to="{ name: 'api' }">archive</router-link>
      </div>
      <div>
        <base-basic-input
          class="input-frame float-left bg-dark-800"
          v-model="query.value"
          @keyup.enter="searchMovie"
        ></base-basic-input>
        <p class="font-light italic pt-2 pl-1 float-left">
          <span
            class="hover:cursor-pointer hover:opacity-20"
            @click="searchMovie"
          >
            search
          </span>
          <span> / </span>
          <span class="hover:opacity-20">advanced</span>
        </p>
      </div>

      <div class="m-5">
        <router-link :to="{ name: 'settings' }">settings</router-link>
      </div>

      <slot name="default"></slot>
    </div>
  </header>
</template>

<style scoped>
.input-frame {
  border-bottom: 1px solid white;
  background-color: black;
}

.header {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 100;
}

</style>
