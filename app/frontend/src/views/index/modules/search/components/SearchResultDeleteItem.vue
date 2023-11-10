<script setup lang="ts">
import { UseIndexSearchStore } from '@/store/IndexSearchStore';
import { UseIndexStore } from '@/store/IndexStore';

interface ComponentProps {
  docId: string;
  imdbId: string;
}

interface ComponentEmits {
  (e: "close"): void;
}

const indexStore = UseIndexStore()
const IndexSearchStore = UseIndexSearchStore()

const props = defineProps<ComponentProps>();
const emits = defineEmits<ComponentEmits>();

const deleteItem = async () => {
  const response = await indexStore.deleteMovie(props.docId);
  if (response) {
    IndexSearchStore.deleteDocByImdbId(props.docId);
  }
  emits('close')
}

</script>

<template>
  <div class="grid grid-cols-2 gap-1">
    <p class="col-span-2">Sure you wanna delete this movie data?</p>
    <base-basic-button @pressed="deleteItem">yes</base-basic-button>
    <base-basic-button @pressed="emits('close')">no</base-basic-button>
  </div>
</template>

<style scoped></style>
