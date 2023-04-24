<script setup lang="ts">
import { ImdbApiService } from "@/services/imdbApi/ImdbApiService";
import { UseArchiveSearchStore } from "@/store/archiveSearch";

const useArchiveSearchStore = UseArchiveSearchStore();

const isLoading = ref(true);

const archiveMovie = async (imdbId: string) => {
  const response = await ImdbApiService.archiveMovie(imdbId);
  console.log(response);
  if (response && response.data === 201) {
    useArchiveSearchStore.removeMovie(imdbId);
  }
};
</script>

<template>
  <app-header-archive></app-header-archive>
  <div class="mx-40">
    <div
      v-if="
        useArchiveSearchStore.searchResults &&
        useArchiveSearchStore.searchResults.length > 0
      "
      class="grid grid-cols-4 gap-1 m-4"
    >
      <div
        class="flex flex-col mb-10 w-full"
        v-for="movie in useArchiveSearchStore.searchResults"
        :key="movie.id"
      >
        <archive-api-search-result
          :movie="movie"
          @clicked="archiveMovie"
        ></archive-api-search-result>
      </div>
    </div>
  </div>
</template>

<style lang="postcss" scoped></style>
