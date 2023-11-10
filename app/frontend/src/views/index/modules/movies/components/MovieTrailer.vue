<script setup lang="ts">

interface ComponentProps {
  movieTrailerLink: string | null;
  movieTrailerImgLink: string;
}

const props = defineProps<ComponentProps>();

</script>

<template>
    <div>
        <div class=" t-6 justify-self-center">
            <span class="text-xl"></span>
        </div>
        <div class="justify-self-center">
            <a :href="`https://www.youtube.com/watch?v=${movieTrailerLink}`">
            <img
                class="trailer-img rounded-full"
                :src="`https://image.tmdb.org/t/p/w500${movieTrailerImgLink}`"
                alt="Trailer image"
            />
            </a>
        </div>
    </div>
</template>

<style scoped lang="postcss">
.trailer-img {
    object-fit: none;
    width: 250px;
    height: 250px;
  }
</style>