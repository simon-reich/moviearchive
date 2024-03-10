<script setup lang="ts">
import { IndexMovieDto } from "@/services/api/dtos/index-movie.dto";
import { UseApiStore } from "@/store/ApiStore";
import { UseIndexStore } from "@/store/IndexStore";
import { ref } from "vue";

const apiStore = UseApiStore();
const indexStore = UseIndexStore();

const loadingMovieId = ref<number | null>(null);
const loadingProgress = ref<number>(0);
const showSuccessMessage = ref(false);
const showFailMessage = ref(false);

const displaySuccessMessage = () => {
  showSuccessMessage.value = true;
  setTimeout(() => {
    showSuccessMessage.value = false;
  }, 2500);
};

const displayFailMessage = () => {
  showFailMessage.value = true;
  setTimeout(() => {
    showFailMessage.value = false;
  }, 2500);
};

const indexMovie = async (tmdbId: number) => {
  const dto: IndexMovieDto = {
    index_name: await indexStore.getSelectedOrDefault(),
    tmdb_id: tmdbId,
    wikipedia: true,
  }
  loadingMovieId.value = tmdbId;
  startLoadingInterall();
  const response = await apiStore.indexMovie(dto);
  console.log(response);
  if (response && response.status === 200 && response.data === 201) {
    displaySuccessMessage();
    loadingProgress.value = 100;
    apiStore.removeSearchResult(dto.tmdb_id);
  } else if (response && response.status === 200 && !response.data) {
    displayFailMessage();
    loadingProgress.value = 100;
  }
};

const startLoadingInterall = () => {
    const interval = setInterval( () => {
    loadingProgress.value += 7;
    if (loadingProgress.value >= 100) {
      clearInterval(interval);
      loadingMovieId.value = null;
      loadingProgress.value = 0;
    }
  }, 200);
};
</script>

<template>
  <app-header-api-search></app-header-api-search>

  <div class="p-18">
    <div
      v-if="
        apiStore.searchResults &&
        apiStore.searchResults.length > 0
      "
      class="grid grid-cols-5 gap-1 m-1"
    >
      <div
        v-for="(movie, index) in apiStore.searchResults"
        :key="movie.id"
        class="flex flex-row w-full movie-item"
        :style="{ 'animation-delay': `${index * 0.1}s` }"
      >
        <api-api-search-result
          :movie="movie"
          @clicked="indexMovie(movie.id)"
        ></api-api-search-result>

        <div v-if="loadingMovieId === movie.id" class="loader">
          <div class="progress-bar" :style="{ width: `${loadingProgress}%` }"></div>
        </div>
      </div>
    </div>
  </div>

  <!-- Message -->
  <div v-if="showSuccessMessage || showFailMessage">
    <base-basic-message>
      <div v-if="showSuccessMessage">
        <p>movie successfully indexed</p>
      </div>
      <div v-if="showFailMessage">
        <p>movie already indexed</p>
      </div>
    </base-basic-message>
  </div>
</template>

<style scoped>
.movie-item {
  animation: fadeInUp 0.5s ease-in-out;
  opacity: 0;
  animation-fill-mode: forwards;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.loader {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.progress-bar {
  background-color: black;
  height: 100%;
  width: 0;
  transition: width 0.2s ease;
}
</style>
