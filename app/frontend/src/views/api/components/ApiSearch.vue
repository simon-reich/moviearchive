<script setup lang="ts">
import { IndexMovieDto } from "@/services/api/dtos/index-movie.dto";
import { UseApiStore } from "@/store/ApiStore";
import { UseIndexStore } from "@/store/IndexStore";

const apiStore = UseApiStore();
const indexStore = UseIndexStore();

const indexMovie = async (tmdbId: number) => {
  const dto: IndexMovieDto = {
    index_name: await indexStore.getSelectedOrDefault(),
    tmdb_id: tmdbId,
  }
  apiStore.indexMovie(dto);
};
</script>

<template>
  <app-header-api-search></app-header-api-search>
  <div class="p-18">
    <div
      v-if="
        apiStore.searchResults &&
        apiStore.searchResults.length > 0
      "
      class="grid grid-cols-5 gap-1 m-1"
    >
      <div
        class="flex flex-row w-full"
        v-for="movie in apiStore.searchResults"
        :key="movie.id"
      >
        <api-api-search-result
          :movie="movie"
          @clicked="indexMovie(movie.id)"
        ></api-api-search-result>
      </div>
    </div>
  </div>
</template>

<style lang="postcss" scoped></style>
