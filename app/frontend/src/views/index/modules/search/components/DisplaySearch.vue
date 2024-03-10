<script setup lang="ts">
import { UseIndexSearchStore } from "@/store/IndexSearchStore";

const indexSearchStore = UseIndexSearchStore();

onBeforeMount(async () => {
  indexSearchStore.aggregateHighlights()
});
</script>

<template>
  <app-header-basic-search></app-header-basic-search>

  <div
    v-if="
      indexSearchStore.searchResults &&
      indexSearchStore.searchResults.length > 0"
  > 
    <div>
      <index-modules-search-search-results 
        :searchResults="indexSearchStore.searchResults"
        :highlightAggregation="indexSearchStore.highlightAggregation 
          ? indexSearchStore.highlightAggregation 
          : null" 
      ></index-modules-search-search-results>
    </div>

  </div>
</template>

<style scoped>
</style>
