<script setup lang="ts">
import { TmdbApiSearchResult } from "@/interfaces/TmdbApiSearchResult";

interface ComponentProps {
  movie: TmdbApiSearchResult;
}

interface ComponentEmits {
  (event: "clicked", value: number): void;
}

const props = defineProps<ComponentProps>();
const emits = defineEmits<ComponentEmits>();

const baseImageUrl = 'https://image.tmdb.org/t/p/'
const tmdbImageSize = 'w342'
const releaseYear = props.movie.release_date ? props.movie.release_date.substring(0, 4) : props.movie.release_date;
const hover = ref(false);

const clicked = async (tmdbId: number) => {
  emits("clicked", tmdbId);
};
</script>

<template>
  <div
    class="relative"
    :searchResult="movie"
    @mouseenter="hover = true"
    @mouseleave="hover = false"
  >
    <img
      :class="hover ? 'courser-pointer opacity-20' : ''"
      :src="movie.poster_path? `${baseImageUrl}${tmdbImageSize}${movie.poster_path}` : '/img/poster-black.png'"
      alt="movie poster"
      @click="clicked(movie.id)"
    />
    <div 
      class="center-text text-5xl font-extrabold backdrop-blur-md z-10"
      @click="clicked(movie.id)"
    >
      <div v-if="hover">
        <p>{{ movie.title }}</p>
        <p>{{ releaseYear }}</p>
      </div>
    </div>
    <div 
      v-if="!movie.poster_path" 
      class="center-text text-5xl font-extrabold text-light-100"
      @click="clicked(movie.id)"
    >
      <div class="">
        <p>{{ movie.title }}</p>
        <p>{{ releaseYear }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped>
.center-text {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}
</style>
