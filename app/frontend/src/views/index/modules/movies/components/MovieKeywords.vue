<script setup lang="ts">

interface ComponentProps {
  keywordsKey: string;
  keywordsValue: string[] | null;
  
}

const props = defineProps<ComponentProps>();

</script>

<template>
  <div>
    <div class="subgrid mr-7">
      <index-modules-movies-movie-info-list
        :infoSingular="'Keyword'"
        :infoMultiple="'Keywords'"
        :infoKey="keywordsKey"
        :infoValue="keywordsValue "
      ></index-modules-movies-movie-info-list>
    </div>
  </div>
</template>

<style scoped lang="postcss">
.subgrid {
    display: grid;
    gap: 0.2em;
    grid-template-columns: 1fr 3fr;
}
</style>