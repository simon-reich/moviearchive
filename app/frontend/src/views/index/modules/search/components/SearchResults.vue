<script setup lang="ts">
import { HighlightAggregation } from "@/interfaces/HighlightAggregation";
import { IndexSearchResult } from "@/interfaces/IndexSearchResult";
import { UseIndexStore } from "@/store/IndexStore";

interface FieldsToTextMap {
  [key: string]: string;
}

interface ComponentProps {
  searchResults: IndexSearchResult[];
  highlightAggregation?: HighlightAggregation[];
}

const props = defineProps<ComponentProps>();

const indexStore = UseIndexStore();

const fieldsToTextMap = ref<FieldsToTextMap | null>(null);

const hoveredIndex = ref<string | null>(null);
const hoveredMovie = ref<IndexSearchResult | null>(null);
const mouseX = ref(0);
const mouseY = ref(0);

const handleMouseMove = (event: MouseEvent) => {
  mouseX.value = event.pageX;
  mouseY.value = event.pageY;
};

const handleMouseEnter = (movie: IndexSearchResult) => {
  setHoveredIndex(movie.imdb_id);
  hoveredMovie.value = movie;
};

const handleMouseLeave = () => {
  clearHoveredIndex();
  hoveredMovie.value = null;
};

const setHoveredIndex = (imdbId: string) => {
  hoveredIndex.value = imdbId;
};

const clearHoveredIndex = () => {
  hoveredIndex.value = null;
};

const getHighlightAsText = (field: string) => {
  const lastIndex = field.lastIndexOf('.');
  if(lastIndex != -1) {
    field = field.substring(0, lastIndex);
  }
  if (fieldsToTextMap.value) {
    return fieldsToTextMap.value[field];
  }
}

window.addEventListener('mousemove', handleMouseMove);

onBeforeMount(async () => {
  const response = await indexStore.getFieldsAsTextMap();
  if(response) {
    fieldsToTextMap.value = response.data;
  }
});
</script>

<template>
  <div class="pt-18 mx-100 my-10">
    <div
      class="grid grid-cols-4 gap-1"
      v-for="movie in searchResults" :key="movie.imdb_id"
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
        @mouseenter="handleMouseEnter(movie)"
        @mouseleave="handleMouseLeave"
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

  <!-- Card to display on hover -->
  <div 
    v-if="hoveredMovie && highlightAggregation && highlightAggregation.length > 0" 
    class="hover-card" 
    :style="{ top: mouseY + 20 + 'px', left: mouseX + 20 + 'px' }"
  >
    <p v-for="highlight in hoveredMovie?.highlight" :key="highlight.field">
      <strong>{{ getHighlightAsText(highlight.field) }}</strong>
    </p>
    <p class="text-green-700 mt-2">
      <strong>{{ hoveredMovie.score }}</strong>
    </p>
  </div>
</template>

<style scoped>
.hovered {
  opacity: .2;
  cursor: pointer;
}

.hover-card {
  position: absolute;
  background: white;
  border: 1px solid #ccc;
  padding: 10px;
}
</style>
