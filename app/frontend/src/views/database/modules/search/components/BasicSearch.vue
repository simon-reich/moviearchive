<script setup lang="ts">
import { router } from "@/routes";
import { useSearchResultsStore } from "@/store/searchResults";

const searchResultsStore = useSearchResultsStore();

const toMovie = async (imdbId: string) => {
  router.push({ name: "database.movies", params: { id: imdbId } });
};
</script>

<template>
  <app-header-basic-search></app-header-basic-search>
  <div
    v-if="
      searchResultsStore.searchResults &&
      searchResultsStore.searchResults.length > 0
    "
    class="m-10 flex flex-col justify-center items-center gap-1"
  >
    <div
      class="hover:opacity-20 hover:cursor-pointer"
      v-for="movie in searchResultsStore.searchResults"
      :key="movie.id"
      @click="toMovie(movie.id)"
    >
      <span class="font-semibold">{{ movie.title }}</span>
      <span> ({{ movie.year }}, </span>
      <span>{{ movie.runtime }}min, </span>
      <span v-for="(genre, index) in movie.genre" :key="genre">
        <span>{{ genre }}</span>
        <span v-if="movie.genre.length > 1 && index < movie.genre.length - 1"
          >,
        </span> </span
      ><span> )</span>
    </div>
  </div>
</template>

<style scoped>
.list {
  display: grid;
  grid-template-columns: 2fr 2fr 1fr 2fr 2fr 3fr 1fr;
}
</style>
