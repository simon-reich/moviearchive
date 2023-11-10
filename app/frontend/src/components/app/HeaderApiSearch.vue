<script setup lang="ts">
import { UseApiStore } from "@/store/ApiStore";

const useApiStore = UseApiStore();

const query = ref("");

const searchMovie = async () => {
  await useApiStore.getSearchResults(query.value);
};
</script>

<template>
  <header class="sticky h-18 bg-dark-800 text-white py-1">
    <div
      class="h-full flex justify-between items-center container mx-auto gap-2"
    >
      <div class="m-5">
        <router-link :to="{ name: 'index.search' }">search</router-link>
      </div>
      <div>
        <base-basic-input
          class="input-frame float-left bg-dark-800"
          v-model="query"
          @keyup.enter="searchMovie"
        ></base-basic-input>
        <p class="font-light italic pt-2 pl-1 float-left">
          <span
            class="hover:cursor-pointer hover:opacity-20"
            @click="searchMovie"
          >
            search to archive
          </span>
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
