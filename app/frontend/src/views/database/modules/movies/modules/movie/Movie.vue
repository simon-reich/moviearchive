<script setup lang="ts">
import { DatabaseService } from "@/services/database/DatabaseService";

interface ComponentProps {
  id: string;
}

const props = defineProps<ComponentProps>();

const movie = ref();

const fullCast = ref(false);
const wikipedia = ref(false);

const toggleFullCast = () => {
  fullCast.value = !fullCast.value;
};

const toggleWikipedia = () => {
  wikipedia.value = !wikipedia.value;
};

onMounted(async () => {
  const response = await DatabaseService.getById(props.id);
  const data = await response[0]._source;
  for (let i = 0; i < Object.keys(data).length; i++) {
    const key = Object.keys(data)[i];
    data[key] = { key: key, value: data[key] };
  }
  movie.value = data;
});
</script>

<template>
  <app-header-basic-search></app-header-basic-search>

  <div v-if="movie" class="m-30">
    <div class="grid grid-cols-2 gap-4 text-shadow-md gap-">
      <div class="subgrid mr-7">
        <div class="col-span-2 text-5xl font-extrabold mb-10">
          <a class="hover:opacity-20" :href="movie.imdbLink.value">
            {{ movie.title.value }}
          </a>
        </div>

        <div>
          <p class="font-semibold">Released</p>
        </div>
        <div>
          <base-db-link
            :field="movie.releaseDate.key"
            :value="movie.releaseDate.value"
            :searchOption="'exact'"
          >
          </base-db-link>
        </div>

        <div v-if="movie.originalTitle.value !== ''">
          <p class="font-semibold">Original Title</p>
        </div>
        <div v-if="movie.originalTitle.value !== ''">
          <p>{{ movie.originalTitle.value }}</p>
        </div>

        <div>
          <p class="font-semibold">Runtime</p>
        </div>
        <div>
          <p>{{ movie.runtime.value }} min</p>
        </div>

        <div class="font-semibold">
          <p v-if="movie.genreList.value.length === 1">Genre</p>
          <p v-if="movie.genreList.value.length > 1">Genres</p>
        </div>
        <div>
          <span v-for="(obj, index) in movie.genreList.value" :key="obj"
            ><base-db-link
              :field="movie.genreList.key"
              :value="obj"
              :searchOption="'exact'"
            >
              <span
                v-if="
                  movie.genreList.value.length > 1 &&
                  index < movie.genreList.value.length - 1
                "
                >,
              </span>
            </base-db-link>
          </span>
        </div>

        <div class="font-semibold">
          <p>Summary</p>
        </div>
        <div>
          <p class="text-justify">{{ movie.plot.value }}</p>
        </div>

        <div class="font-semibold">
          <p v-if="movie.directorList.value.length === 1">Director</p>
          <p v-if="movie.directorList.value.length > 1">Directors</p>
        </div>
        <div class="text-justify">
          <span v-for="(obj, index) in movie.directorList.value" :key="obj.id">
            <base-db-link
              :field="movie.directorList.key"
              :value="obj.name"
              :searchOption="'exact'"
            >
              <span
                v-if="
                  movie.directorList.value.length > 1 &&
                  index < movie.directorList.value.length - 1
                "
                >,
              </span>
            </base-db-link>
          </span>
        </div>

        <div class="text-justify font-semibold">
          <p v-if="movie.writerList.value.length === 1">Writer</p>
          <p v-if="movie.writerList.value.length > 1">Writers</p>
        </div>
        <div>
          <span v-for="(obj, index) in movie.writerList.value" :key="obj.id">
            <base-db-link
              :field="movie.writerList.key"
              :value="obj.name"
              :searchOption="'exact'"
            >
              <span
                v-if="
                  movie.writerList.value.length > 1 &&
                  index < movie.writerList.value.length - 1
                "
                >,
              </span>
            </base-db-link>
          </span>
        </div>

        <div class="text-justify font-semibold">
          <p v-if="movie.starList.value.length > 0">With</p>
        </div>
        <div>
          <span v-for="(obj, index) in movie.starList.value" :key="obj.id">
            <base-db-link
              :field="movie.starList.key"
              :value="obj.name"
              :searchOption="'exact'"
            >
              <span
                v-if="
                  movie.starList.value.length > 1 &&
                  index < movie.starList.value.length - 1
                "
                >,
              </span>
            </base-db-link>
          </span>
        </div>

        <div class="text-justify font-semibold">
          <p v-if="movie.countryList.value.length === 1">Country</p>
          <p v-if="movie.countryList.value.length > 1">Countries</p>
        </div>
        <div>
          <span v-for="(obj, index) in movie.countryList.value" :key="obj">
            <base-db-link
              :field="movie.countryList.key"
              :value="obj"
              :searchOption="'exact'"
            >
              <span
                v-if="
                  movie.countryList.value.length > 1 &&
                  index < movie.countryList.value.length - 1
                "
                >,
              </span>
            </base-db-link>
          </span>
        </div>

        <div class="text-justify font-semibold">
          <p v-if="movie.languageList.value.length === 1">Language</p>
          <p v-if="movie.languageList.value.length > 1">Languages</p>
        </div>
        <div>
          <span v-for="(obj, index) in movie.languageList.value" :key="obj">
            <base-db-link
              :field="movie.languageList.key"
              :value="obj"
              :searchOption="'exact'"
            >
              <span
                v-if="
                  movie.languageList.value.length > 1 &&
                  index < movie.languageList.value.length - 1
                "
                >,
              </span>
            </base-db-link>
          </span>
        </div>

        <div class="text-justify font-semibold">
          <p v-if="movie.companyList.value.length > 0">Produced by</p>
        </div>
        <div>
          <span v-for="(obj, index) in movie.companyList.value" :key="obj">
            <base-db-link
              :field="movie.companyList.key"
              :value="obj.name"
              :searchOption="'exact'"
            >
              <span
                v-if="
                  movie.companyList.value.length > 1 &&
                  index < movie.companyList.value.length - 1
                "
                >,
              </span>
            </base-db-link>
          </span>
        </div>

        <div class="font-semibold">
          <p>Content Rating</p>
        </div>
        <div>
          <p>{{ movie.contentRating.value }}</p>
        </div>

        <div class="text-justify font-semibold">
          <p v-if="movie.keywordList.value.length === 1">Keyword</p>
          <p v-if="movie.keywordList.value.length > 1">Keywords</p>
        </div>
        <div>
          <span v-for="(obj, index) in movie.keywordList.value" :key="obj">
            <base-db-link
              :field="movie.keywordList.key"
              :value="obj"
              :searchOption="'exact'"
            >
              <span
                v-if="
                  movie.keywordList.value.length > 1 &&
                  index < movie.keywordList.value.length - 1
                "
                >,
              </span>
            </base-db-link>
          </span>
        </div>
        <div class="font-semibold">
          <p>IMDb Rating</p>
        </div>
        <div>
          <a
            class="hover:opacity-20"
            :href="movie.imdbLink.value + '/reviews?ref_=tt_urv'"
          >
            <p>{{ movie.imdbRating.value }}</p>
          </a>
        </div>

        <div class="font-semibold">
          <p>IMDb Votes</p>
        </div>
        <div>
          <p>{{ movie.imdbVotes.value }}</p>
        </div>
      </div>

      <div class="overflow-hidden justify-self-center">
        <a :href="movie.wikiLink.value">
          <img
            class="rounded-2xl hover:opacity-80 image"
            :src="movie.imageLink.value"
            alt="Movie Poster"
          />
        </a>
      </div>

      <div class="col-span-2 justify-self-center mt-10 font-semibold">
        <p v-if="movie.actorList.value.length > 1">Starring</p>
      </div>
      <div class="col-span-2 justify-self-center text-center">
        <span v-for="(obj, index) in movie.actorList.value" :key="obj.id">
          <base-db-link
            :field="movie.actorList.key"
            :value="obj.name"
            :searchOption="'exact'"
          >
            <span
              v-if="
                movie.actorList.value.length > 1 &&
                index < movie.actorList.value.length - 1
              "
              >,
            </span>
          </base-db-link>
        </span>
      </div>

      <div
        class="col-span-2 justify-self-center mt-10 font-semibold text-center hover:cursor-pointer"
        @click="toggleFullCast()"
      >
        <p>Full Cast</p>
        <icon-iconoir:arrow-down v-if="!fullCast"></icon-iconoir:arrow-down>
      </div>
      <div v-if="fullCast" class="col-span-2">
        <div>
          <span v-for="obj in movie.fullCast.value.actors" :key="obj.id">
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
              <span v-for="item in obj.items" :key="item.id">
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
      </div>

      <div
        class="col-span-2 justify-self-center mt-10 font-semibold text-center hover:cursor-pointer"
        @click="toggleWikipedia()"
      >
        <p>Wikipedia</p>
        <icon-iconoir:arrow-down v-if="!wikipedia"></icon-iconoir:arrow-down>
      </div>
      <div
        v-if="wikipedia"
        class="text-justify col-span-2 mt-10"
        v-html="movie.wikiTextFullHtml.value"
      ></div>

      <div class="col-span-2 mt-6 justify-self-center">
        <span class="text-xl">TRAILER</span>
      </div>
      <div class="col-span-2 justify-self-center">
        <a :href="movie.trailer.value.link">
          <img
            class="trailer-img rounded-full"
            :src="movie.trailer.value.thumbnailUrl"
            alt="Trailer image"
          />
        </a>
      </div>

      <!-- <div class="w-50 h-50">
      <img
        v-for="poster in movie.posterList"
        :key="poster.id"
        :src="poster.link"
        alt="poster"
      />
    </div> -->
    </div>
  </div>
</template>

<style scoped lang="postcss">
.trailer-img {
  object-fit: none;
  width: 350px;
  height: 350px;
}

.subgrid {
  display: grid;
  gap: 0.2em;
  grid-template-columns: 1fr 3fr;
}

.jobs {
  display: grid;
  gap: 2em;
  grid-template-columns: 1fr 1fr 1fr 1fr;
}
</style>
