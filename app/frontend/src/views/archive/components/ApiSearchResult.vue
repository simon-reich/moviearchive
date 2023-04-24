<script setup lang="ts">
import { ImdbApiSearchResult } from "@/interfaces/ImdbApiSearchResult";

interface ComponentProps {
  movie: ImdbApiSearchResult;
}

interface ComponentEmits {
  (event: "clicked", value: string): void;
}

const props = defineProps<ComponentProps>();
const emits = defineEmits<ComponentEmits>();

const hover = ref(false);

const clicked = async (imdbId: string) => {
  emits("clicked", imdbId);
};

const lo = () => {
  console.log(hover.value);
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
      :src="movie.image"
      alt="movie poster"
      @click="clicked(movie.id)"
    />
    <div class="text-md absolute top-2 left-2">
      <div v-if="hover">
        <p>{{ movie.title }}</p>
        <p>{{ movie.description }}</p>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
