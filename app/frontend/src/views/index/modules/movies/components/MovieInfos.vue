<script setup lang="ts">
import { Movie } from "@/interfaces/Movie";

interface ComponentProps {
  movie: Movie;
}

const props = defineProps<ComponentProps>();

// const distinctJobs: Set<string> = new Set(
//     props.movie.full_crew.value
//         .map((member) => member.department)
//         .filter((job) => job !== null) 
//         .map((job) => job!)
// );
// const distinctJobsArray: string[] = Array.from(distinctJobs);
// console.log(distinctJobsArray);

// const directorJobs: string[] = distinctJobsArray.filter((job) =>
//     job.toLowerCase().includes("casting")
// );
// console.log(directorJobs);

</script>

<template>
    <div class="subgrid mr-7">
      <!-- TITLE -->
      <div class="col-span-2 text-5xl font-extrabold mb-10 pt-4">
        <a class="hover:opacity-20" :href="movie.imdb_link.value ? movie.imdb_link.value : ''">
          {{ movie.title.value }}
        </a>
      </div>

      <!-- YEAR -->
      <index-modules-movies-movie-info-item
        :info="'Released'"
        :infoValue="movie.year.value"
        :infoKey="movie.year.key"
      ></index-modules-movies-movie-info-item>

      <!-- ORIGINAL TITLE -->
      <index-modules-movies-movie-info-item
        v-if="movie.original_title.value"
        :info="'Original title'"
        :infoValue="movie.original_title.value"
      ></index-modules-movies-movie-info-item>

      <!-- RUNTIME -->
      <index-modules-movies-movie-info-item
        v-if="movie.runtime.value"
        :info="'Runtime'"
        :infoValue="movie.runtime.value"
      ></index-modules-movies-movie-info-item>

      <!-- GENRES -->
      <index-modules-movies-movie-info-list
        :infoSingular="'Genre'"
        :infoMultiple="'Genres'"
        :infoKey="movie.genre_list.key"
        :infoValue="movie.genre_list.value"
      ></index-modules-movies-movie-info-list>

      <!-- PLOT -->
      <index-modules-movies-movie-info-item
        :info="'Plot'"
        :infoValue="movie.synopsis.value"
        :textStyling="'text-justify'"
      ></index-modules-movies-movie-info-item>

      <!-- DIRECTOR -->
      <index-modules-movies-movie-info-list
        :infoSingular="'Director'"
        :infoMultiple="'Directors'"
        :infoKey="movie.director_list.key"
        :infoValue="movie.director_list.value"
      ></index-modules-movies-movie-info-list>

      <!-- WRITER -->
      <index-modules-movies-movie-info-list
        :infoSingular="'Writer'"
        :infoMultiple="'Writers'"
        :infoKey="movie.writer_list.key"
        :infoValue="movie.writer_list.value"
      ></index-modules-movies-movie-info-list>

      <!-- MAIN CAST -->
      <index-modules-movies-movie-info-list
        :infoSingular="'With'"
        :infoMultiple="'With'"
        :infoKey="movie.main_cast.key"
        :infoValue="movie.main_cast.value"
      ></index-modules-movies-movie-info-list>

      <!-- COUNTRIES -->
      <index-modules-movies-movie-info-list
        :infoSingular="'Country'"
        :infoMultiple="'Countries'"
        :infoKey="movie.country_list.key"
        :infoValue="movie.country_list.value"
      ></index-modules-movies-movie-info-list>

      <!-- LANGUAGES -->
      <index-modules-movies-movie-info-list
        :infoSingular="'Language'"
        :infoMultiple="'Languages'"
        :infoKey="movie.language_list.key"
        :infoValue="movie.language_list.value"
      ></index-modules-movies-movie-info-list>

      <!-- PRODUCTION -->
      <index-modules-movies-movie-info-list
        :infoSingular="'Produced by'"
        :infoMultiple="'Produced by'"
        :infoKey="movie.company_list.key"
        :infoValue="movie.company_list.value"
      ></index-modules-movies-movie-info-list>
      

      <!-- CONTENT RATING -->
      <index-modules-movies-movie-info-item
        :info="'Content rating'"
        :infoValue="movie.content_rating.value"
      ></index-modules-movies-movie-info-item>

      <!-- IMDB RATING -->
      <index-modules-movies-movie-info-item
        :info="'IMDb rating'"
        :infoValue="movie.imdb_rating.value"
        :link="`${movie.imdb_link.value}/reviews?ref_=tt_urv`"
      ></index-modules-movies-movie-info-item>

      <!-- IMDB VOTES -->
      <index-modules-movies-movie-info-item
        :info="'IMDb votes'"
        :infoValue="movie.imdb_votes.value"
      ></index-modules-movies-movie-info-item>
  </div>
</template>

<style scoped lang="postcss">
.subgrid {
    display: grid;
    gap: 0.2em;
    grid-template-columns: 1fr 3fr;
}
</style>