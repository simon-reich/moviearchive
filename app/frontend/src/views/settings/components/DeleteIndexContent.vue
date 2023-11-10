<script setup lang="ts">
import { DatabaseService } from '@/services/database/DatabaseService';
import { UseIndexStore } from '@/store/IndexStore';

interface ComponentProps {
  indexName: string;
}

interface ComponentEmits {
  (e: "close"): void;
}

const IndexStore = UseIndexStore()

const props = defineProps<ComponentProps>();
const emits = defineEmits<ComponentEmits>();

const deleteIndex = async () => {
  const response_index = await IndexStore.deleteIndex(props.indexName)
  const response_db = await DatabaseService.deleteIndexByName(props.indexName)
  console.log(`${response_index} ${response_db}`);
  emits('close');
}
</script>

<template>
  <p>Sure u wanna delete {{ indexName }}?</p>
  <div class="grid grid-cols-2 gap-1">
    <base-basic-button @pressed="deleteIndex">yes</base-basic-button>
    <base-basic-button @pressed="emits('close')">no</base-basic-button>
  </div>
</template>

<style scoped>
</style>
