<script setup lang="ts">

interface ComponentProps {
  posterLink: string;
}

const props = defineProps<ComponentProps>();

</script>

<template>
        <img
          class="hover:opacity-80 image"
          :src="`https://image.tmdb.org/t/p/original${posterLink}`"
          alt="Movie Poster"
        />
</template>

<style scoped lang="postcss">
.image {
  width: 100%; /* Make the image take 100% width of its container */
  height: 100%; /* Make the image take 100% height of its container */
  object-fit: cover;
}
</style>