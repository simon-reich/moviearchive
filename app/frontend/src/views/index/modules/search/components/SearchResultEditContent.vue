<script setup lang="ts">
import { MovieEditableFields } from '@/interfaces/MovieEditableFields';
import { UseIndexStore } from '@/store/IndexStore';

interface ComponentProps {
  docId: string;
  imdbId: string;
}

interface ComponentEmits {
  (e: "close"): void;
}

const indexStore = UseIndexStore();

const props = defineProps<ComponentProps>();
const emits = defineEmits<ComponentEmits>();

const movieEditValues = ref<MovieEditableFields>({
    doc_id: props.docId,
    imdb_id: props.imdbId,
    watched: false,
    personal_notes: "",
    personal_rating: null,
})

const ratings = [0,1,2,3,4,5,6,7,8,9,10]

const editMovie = async () => {
  await indexStore.editMovie(movieEditValues.value)
  emits('close');
}

onBeforeMount(async () => {
  const response = await indexStore.getEditableMovieValues(props.imdbId);
  if (response) {
    movieEditValues.value.watched = response[0].watched ? response[0].watched : false;
    movieEditValues.value.personal_notes = response[0].personal_notes ? response[0].personal_notes : "";
    movieEditValues.value.personal_rating = response[0].personal_rating ? response[0].personal_rating : null;
  } 
});
</script>

<template>
  <div class="grid grid-cols-2 gap-1">
    <div class="grid grid-cols-2 gap-1">
      <p class="justify-start">watched:</p>
      <base-basic-checkbox class="justify-end" v-model="movieEditValues.watched"></base-basic-checkbox>
    </div>
    
    <div class="grid grid-cols-2 gap-1">
      <p class="justify-start">rating:</p>
      <base-basic-select class="justify-end" 
        v-model="movieEditValues.personal_rating"
        :items="ratings"
      ></base-basic-select>
    </div>
    
    <div class="col-span-2">
      <p class="justify-start">personal notes:</p>
      <base-basic-textarea class="" :type="'textfield'" v-model="movieEditValues.personal_notes"></base-basic-textarea>
    </div>

    <div class="mt-4">
      <base-basic-button @pressed="editMovie">edit</base-basic-button>
    </div>
  </div>
</template>

<style scoped></style>
