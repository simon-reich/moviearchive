<script setup lang="ts">
import { Image } from "@/interfaces/Image";
import { IndexService } from "@/services/index/IndexService";
import { UseIndexSearchStore } from "@/store/IndexSearchStore";

interface ComponentProps {
  imdbId: string;
}

const indexSearchStore = UseIndexSearchStore();

const props = defineProps<ComponentProps>();
const movie = ref();
const backdrop = ref('');
const fullCast = ref(false);

const toggleFullCast = () => {
  fullCast.value = !fullCast.value;
};

onBeforeMount(async () => {
  const response = await indexSearchStore.getMovieByImdbId(props.imdbId)
  if (response.length > 0) {
    const data = await response[0]._source;
    data.doc_id = response[0]._id
    
    // create objects for each movie property with 
    // key=*property as string*
    // value=*value of property*
    // to make property as string available 
    for (let i = 0; i < Object.keys(data).length; i++) {
      const key = Object.keys(data)[i];
      data[key] = { key: key, value: data[key] };
    }
    
    movie.value = data;

    // create list of backdrops and chose random value from it for backdrop variable
    const backdrops = data.backdrop_list.value.filter((item: Image) => item.height >= 720 && item.width >= 1280);
    backdrop.value = backdrops[Math.floor(Math.random() * backdrops.length)].file_path;
  }
});

</script>

<template>
    <!-- blurry fixed background image -->
    <div v-if="backdrop" class="fixed-background">
      <img 
        :src="`https://image.tmdb.org/t/p/original${backdrop}`" 
        alt="Background Image"
      >
  </div>

  <div class="screen">
    <app-header-basic-search></app-header-basic-search>
    
    <div class="grid-container">

      <div class="grid grid-cols-1 gap-10"> 

        <!-- MAIN INFOS -->
        <div v-if="movie" class="grid grid-cols-3 gap-10 bg-transparent text-shadow-md">   
          <!-- movie poster image (left) -->
          <img
            class="hover:opacity-80 image"
            :src="`https://image.tmdb.org/t/p/original${movie.poster.value}`"
            alt="Movie Poster"
          />

          <!-- general movie infos (middle) -->
          <index-modules-movies-movie-infos 
            :movie="movie"
          ></index-modules-movies-movie-infos>
          
          <!-- trailer + keywords (right) -->
          <div class="grid grid-cols-1">
            <!-- trailer -->
            <div class="flex flex-col h-full items-center justify-center">
              <index-modules-movies-movie-trailer 
                :movieTrailerLink="movie.trailer.value ? movie.trailer.value.key : null"
                :movieTrailerImgLink="backdrop"
              ></index-modules-movies-movie-trailer>
            </div>

            <!-- keywords -->
            <div>
              <index-modules-movies-movie-keywords
                class="flex flex-col h-full justify-end"
                :keywordsKey="movie.keyword_list.key"
                :keywordsValue="movie.keyword_list.value ? movie.keyword_list.value : null"
              ></index-modules-movies-movie-keywords>
            </div>
          </div>

        </div>

        <div v-if="movie.wikipedia_summary" class="mx-60">
          <p>{{ movie.wikipedia_summary.value }}</p>
        </div>

        <div v-if="movie.wikipedia_plot" class="mx-60">
          <p>{{ movie.wikipedia_plot.value }}</p>
        </div>
      
        <!-- ADDITIONAL INFOS -->
        <div class="grid grid-cols-3 gap-10 bg-transparent text-shadow-md">
          <!-- cast -->
          <div>
            <index-modules-movies-movie-cast
              class=""
              :fullCast="movie.full_cast.value"
            ></index-modules-movies-movie-cast>
          </div>
          
          <!-- main crew -->
          <div>
            <index-modules-movies-movie-crew-main
              class=""
              :fullCrew="movie.full_crew.value"
            ></index-modules-movies-movie-crew-main>
          </div>

          <!-- additional crew -->
          <div>
            <index-modules-movies-movie-crew-additional
              class=""
              :fullCrew="movie.full_crew.value"
            ></index-modules-movies-movie-crew-additional>
          </div>
        </div>

      </div>
    </div>
  </div>

  

</template>

<style scoped lang="postcss">
.fixed-background {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -10;
}

.fixed-background img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.8;
  filter: blur(10px);
}

.screen {
  display: flex;
  flex-direction: column;
  height: 100vh; 
}

.grid-container {
  flex: 1; /* Fill the remaining vertical space */
  height: calc(100vh - 4.5rem);
}

.image {
  width: 100%; /* Make the image take 100% width of its container */
  height: 100%; /* Make the image take 100% height of its container */
  object-fit: cover;
}
</style>
