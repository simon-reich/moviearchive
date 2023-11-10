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
  const data = await response[0]._source;
  data.doc_id = response[0]._id
  console.log(data);
  
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
});

</script>

<template>
  <app-header-basic-search></app-header-basic-search>

  <!-- blurry fixed background image -->
  <div v-if="backdrop" class="fixed-background">
      <img 
        :src="`https://image.tmdb.org/t/p/original${backdrop}`" 
        alt="Background Image"
      >
  </div>

  <div v-if="movie" class="content p-8 h-full px-10 mx-20">
    <div class="grid grid-cols-3 gap-10 text-shadow-md">
      
      <!-- movie poster image (middle) -->
      <index-modules-movies-movie-poster
        :posterLink="movie.poster.value">
      </index-modules-movies-movie-poster>

       <!-- general movie infos (left) -->
       <index-modules-movies-movie-infos 
        :movie="movie"
      ></index-modules-movies-movie-infos>
      
      <!-- trailer + keywords (right) -->
      <div class="grid grid-cols-1 w-full h-full">
        <!-- trailer -->
        <div class="flex flex-col w-full h-full items-center justify-center">
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

      <!-- cast -->
      <div>
      {{ `https://image.tmdb.org/t/p/original${backdrop}` }}
      {{ `https://image.tmdb.org/t/p/original${movie.poster.value}` }}

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



      <!-- <div class="col-span-2 justify-self-center mt-10 font-semibold">
        <p v-if="movie.main_cast.value.length > 1">Starring</p>
      </div>
      <div class="col-span-2 justify-self-center text-center">
        <span v-for="(obj, index) in movie.main_cast.value" :key="obj.imdbId">
          <base-db-link
            :field="movie.main_cast.key"
            :value="obj"
            :searchOption="'exact'"
          >
            <span
              v-if="
                movie.main_cast.value.length > 1 &&
                index < movie.main_cast.value.length - 1
              "
              >,
            </span>
          </base-db-link>
        </span>
      </div> -->

      <!-- <div
        class="col-span-2 justify-self-center mt-10 font-semibold text-center hover:cursor-pointer"
        @click="toggleFullCast()"
      >
        <p>Full Cast</p>
        <icon-iconoir:arrow-down v-if="!fullCast"></icon-iconoir:arrow-down>
      </div>
      <div v-if="fullCast" class="col-span-2">
        <div>
          <span v-for="obj in movie.fullCast.value.actors" :key="obj.imdbId">
            <div class="grid grid-cols-2 gap-10">
              <div class="justify-self-end">
                <p>{{ obj.asCharacter }}</p>
              </div>
              <base-db-link
                class="justify-self-start"
                :field="movie.fullCast.key"
                :value="obj.name"
                :searchOption="'exact'"
              >
              </base-db-link>
            </div>
          </span>
        </div>

        <div class="">
          <div
            class="col-span-2 justify-self-center mt-5"
            v-for="obj in movie.fullCast.value.others"
            :key="obj.job"
          >
            <p class="text-center mb-2">{{ obj.job }}</p>
            <div class="">
              <span v-for="item in obj.items" :key="item.imdbId">
                <div class="grid grid-cols-2 gap-10">
                  <div class="justify-self-end" v-if="item.description !== ''">
                    <p>{{ item.description }}</p>
                  </div>
                  <div
                    :class="
                      item.description !== ''
                        ? 'justify-self-start'
                        : 'col-span-2 justify-self-center text-center'
                    "
                  >
                    <base-db-link
                      :field="movie.fullCast.key"
                      :value="item.name"
                      :searchOption="'exact'"
                    ></base-db-link>
                  </div>
                </div>
              </span>
            </div>
          </div>
        </div>
      </div> -->

      <!-- <div class="w-50 h-50">
      <img
        v-for="poster in movie.posterList"
        :key="poster.imdbId"
        :src="poster.link"
        alt="poster"
      />
    </div> -->
    </div>
  </div>
</template>

<style scoped lang="postcss">

.jobs {
  display: grid;
  gap: 2em;
  grid-template-columns: 1fr 1fr 1fr 1fr;
}

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

.content {
  position: relative;
  z-index: 10; 
}
</style>
