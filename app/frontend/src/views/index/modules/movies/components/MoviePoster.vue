<script setup lang="ts">

interface ComponentProps {
  posterLink: string;
}

const props = defineProps<ComponentProps>();

</script>

<template>
    <div class="overflow-hidden justify-self-center">
        <img
          class="hover:opacity-80 image"
          :src="`https://image.tmdb.org/t/p/w500${posterLink}`"
          alt="Movie Poster"
        />
    </div>
</template>

<style scoped lang="postcss">
</style>