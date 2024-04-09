<script setup lang="ts">
import { router } from "@/routes";

interface ComponentProps {
  imdbId: string;
  title: string;
  originalTitle?: string | boolean;
  year: number;
  runtime: number;
  genres: string[];
}

const props = defineProps<ComponentProps>();

const toMovie = async (imdbId: string) => {
  router.push({ name: "index.movies", params: { imdbId: imdbId } });
};
</script>

<template>
    <div @click="toMovie(imdbId)">
        <span class="font-semibold">{{ title }}</span>
        <span v-if="originalTitle" class="font-semibold"> ({{ originalTitle }})</span>
        <span> ({{ year }}, </span>
        <span>{{ runtime }}min, </span>
        <span v-for="(genre, index) in genres" :key="genre">
            <span>{{ genre }}</span>
            <span v-if="(genres.length > 1) && (index < genres.length - 1)">, </span> 
        </span>
        <span>)</span>
    </div>
</template>

<style scoped></style>
