<script setup lang="ts">
import { BasicQuery } from "@/interfaces/BasicQuery";
import { router } from "@/routes";
import { useSearchResultsStore } from "@/store/searchResults";

const searchResultsStore = useSearchResultsStore();

const query = ref<BasicQuery>({
  field: import.meta.env.VITE_QUERY_FIELD,
  value: "",
  size: import.meta.env.VITE_DB_DATA_ARRAY_SIZE,
});

const searchMovie = async () => {
  searchResultsStore.getExactResults(query.value);
  router.push({ name: "database.search" });
};
</script>

<template>
  <header class="h-14 bg-dark-800 text-white py-1">
    <div
      class="h-full flex justify-between items-center container mx-auto gap-2"
    >
      <div class="m-5">
        <router-link :to="{ name: 'archive' }">archive</router-link>
      </div>
      <div>
        <base-base-input
          class="input-frame float-left bg-dark-800"
          v-model="query.value"
          @keyup.enter="searchMovie"
        ></base-base-input>
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
</style>
