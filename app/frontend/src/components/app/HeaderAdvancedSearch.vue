<script setup lang="ts">
import { AggregationItem } from "@/interfaces/AggregationItem";
import { router } from "@/routes";
import { DatabaseService } from "@/services/database/DatabaseService";
import { useSearchParametersStore } from "@/store/searchParameters";
import { useSearchResultsStore } from "@/store/searchResults";

const searchResultsStore = useSearchResultsStore();
const searchParametersStore = useSearchParametersStore();

const parameters = toRefs(searchParametersStore.parameters);

const genres = ref<AggregationItem[]>([]);
const languages = ref<AggregationItem[]>([]);
const countries = ref<AggregationItem[]>([]);

const genre = ref("");
const actor = ref("");

const searchMovies = async () => {
  searchResultsStore.getAdvancedSearchResults(searchParametersStore.parameters);
  router.push({ name: "database.search" });
};

const addGenre = () => {
  if (!parameters.genres.value.includes(genre.value)) {
    parameters.genres.value.push(genre.value);
  }
};

const removeGenre = (index: number) => {
  parameters.genres.value.splice(index, 1);
};

const addActor = () => {
  if (!parameters.actors.value.includes(actor.value)) {
    parameters.actors.value.push(actor.value);
    actor.value = "";
  }
};

const removeActor = (index: number) => {
  parameters.actors.value.splice(index, 1);
};

onMounted(async () => {
  genres.value = await DatabaseService.getDistinctValues("genreList");
  languages.value = await DatabaseService.getDistinctValues("languageList");
  countries.value = await DatabaseService.getDistinctValues("countryList");
});
</script>

<template>
  <header class="bg-dark-800 text-white py-1">
    <div
      class="h-full flex justify-between items-start container mx-auto gap-2"
    >
      <div class="m-5">
        <router-link :to="{ name: 'archive' }">archive</router-link>
      </div>
      <div class="grid grid-cols-2 gap-10 m-5">
        <!-- grid 0-0 -->
        <div>
          <p class="font-light italic pt-2 pr-2 float-left">
            <span
              class="hover:cursor-pointer hover:opacity-20"
              @click="searchMovies"
            >
              runtime less then
            </span>
          </p>
          <base-base-input
            class="input-frame w-10 float-left bg-dark-800"
            v-model="parameters.runtime.value"
            @keyup.enter="searchMovies"
          ></base-base-input>
          <p class="font-light italic pt-2 pl-2 float-left">
            <span>min</span>
          </p>
        </div>
        <!-- grid 0-1 -->
        <div>
          <p class="font-light italic pt-2 pr-2 float-left">
            <span
              class="hover:cursor-pointer hover:opacity-20"
              @click="searchMovies"
            >
              released around
            </span>
          </p>
          <base-base-input
            class="input-number float-left bg-dark-800"
            v-model="parameters.year.value"
            @keyup.enter="searchMovies"
          ></base-base-input>
        </div>
        <!-- grid 1-0 -->
        <div>
          <p class="font-light italic pt-2 pr-2 float-left">
            <span
              class="hover:cursor-pointer hover:opacity-20"
              @click="searchMovies"
            >
              content
            </span>
          </p>
          <base-base-input
            class="input-frame frame-left float-left bg-dark-800"
            v-model="parameters.content.value"
            @keyup.enter="searchMovies"
          ></base-base-input>
        </div>
        <!-- grid 1-1 -->
        <div>
          <base-base-input
            class="input-frame frame-right float-left bg-dark-800"
            v-model="parameters.director.value"
            @keyup.enter="searchMovies"
          ></base-base-input>
          <p class="font-light italic pt-2 pl-2 float-left">
            <span
              class="hover:cursor-pointer hover:opacity-20"
              @click="searchMovies"
            >
              director
            </span>
          </p>
        </div>
        <!-- grid 2 -->
        <div class="col-span-2">
          <base-base-select
            class="float-left"
            :items="genres.map((genre) => genre.key)"
            v-model="genre"
            defaultValue="genre"
            @update:modelValue="addGenre"
          >
          </base-base-select>
          <p class="font-light pl-2 float-left">
            <span
              class="hover:cursor-pointer hover:opacity-20 pl-2 text-sm"
              v-for="(genre, index) in parameters.genres.value"
              :key="index"
              @click="removeGenre(index)"
            >
              {{ genre }}
            </span>
          </p>
        </div>
        <!-- grid 3 -->
        <div class="col-span-2">
          <p class="font-light italic pt-2 pr-2 float-left">
            <span
              class="hover:cursor-pointer hover:opacity-20"
              @click="searchMovies"
            >
              starring
            </span>
          </p>
          <base-base-input
            class="input-frame bg-dark-800 float-left"
            v-model="actor"
            @keyup.enter="addActor"
          ></base-base-input>
          <p class="font-light pl-2 float-left">
            <span
              class="hover:cursor-pointer hover:opacity-20 pl-2 text-sm"
              v-for="(actor, index) in parameters.actors.value"
              :key="index"
              @click="removeActor(index)"
            >
              {{ actor }}
            </span>
          </p>
        </div>
        <!-- grid 4-0 -->
        <base-base-select
          class=""
          :items="languages.map((language) => language.key)"
          v-model="parameters.language.value"
          defaultValue="language"
        ></base-base-select>
        <!-- grid 4-1 -->
        <base-base-select
          class=""
          :items="countries.map((country) => country.key)"
          v-model="parameters.country.value"
          defaultValue="country"
        ></base-base-select>
        <!-- grid 5 -->
        <div class="col-span-2">
          <p class="font-light italic pt-2 pr-2 float-left">
            <span
              class="hover:cursor-pointer hover:opacity-20"
              @click="searchMovies"
            >
              full staff
            </span>
          </p>
          <base-base-input
            class="input-frame frame-left float-left bg-dark-800"
            v-model="parameters.staff.value"
            @keyup.enter="searchMovies"
          ></base-base-input>
        </div>
      </div>

      <div class="m-5">
        <p class="">settings</p>
      </div>

      <slot name="default"></slot>
    </div>
  </header>
</template>

<style scoped>
.input-frame {
  border-bottom: 1px solid white;
  background-color: black;
}

.frame-right {
  border-left: 1px solid white;
}

.frame-left {
  border-right: 1px solid white;
}

.input-number {
  border-bottom: 1px solid white;
  background-color: black;
  width: 5em;
}
</style>
