<script setup lang="ts">
import { IndexSearchResult } from "@/interfaces/IndexSearchResult";

interface ComponentProps {
  searchResults: IndexSearchResult[];
}

const props = defineProps<ComponentProps>();
const hoveredIndex = ref<string | null>(null);

</script>

<template>
  <div class="pt-18 mx-100 my-10">
      <div
        class="grid grid-cols-4 gap-1"
        v-for="movie in searchResults"
        :key="movie.imdb_id"
      >
      <!-- search result -->
        <index-modules-search-search-result
          class="col-span-3"
          :class="{ 'hovered': hoveredIndex === movie.imdb_id }"
          :imdbId="movie.imdb_id"
          :title="movie.title"
          :year="movie.year"
          :runtime="movie.runtime"
          :genres="movie.genre"
          @mouseenter="hoveredIndex = movie.imdb_id"
          @mouseleave="hoveredIndex = null"
        ></index-modules-search-search-result>

        <!-- edit button -->
        <div class="flex flex-row w-full justify-end">
          <div             
            @mouseenter="hoveredIndex = movie.imdb_id"
            @mouseleave="hoveredIndex = null"
          >
            <index-modules-search-search-result-edit-button 
              :title="movie.title"
              :docId="movie.doc_id"
              :imdbId="movie.imdb_id"
            >
            </index-modules-search-search-result-edit-button>
          </div>

          <!-- delete button -->
          <div             
            @mouseenter="hoveredIndex = movie.imdb_id"
            @mouseleave="hoveredIndex = null"
          >
            <index-modules-search-search-result-delete-button 
              :title="movie.title"
              :docId="movie.doc_id"
              :imdbId="movie.imdb_id"
            >
            </index-modules-search-search-result-delete-button>
          </div>
        </div>
    
      </div>
    </div>
</template>

<style scoped>
.hovered {
  opacity: .2;
  cursor: pointer;
}
</style>
