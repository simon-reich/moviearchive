<script setup lang="ts">
import { UseIndexStore } from '@/store/IndexStore';
import { IndexFolderDto } from '@/services/index/dtos/index-folder.dto';

interface ComponentEmits {
  (e: "close"): void;
}

const indexStore = UseIndexStore()

const emits = defineEmits<ComponentEmits>();

const indexFolderDto = ref<IndexFolderDto>({
    path: "",
})

const indexFolder = async () => {
  const response = await indexStore.indexFolder(indexFolderDto.value);
  await indexStore.getIndicies();
  console.log(response);
  emits('close');
}
</script>

<template>
  <div class="grid grid-cols-2 gap-1">
    <p>index name:</p>
    <base-basic-input class="input" v-model="indexFolderDto.path"></base-basic-input>

    <div class="mt-4">
      <base-basic-button @pressed="indexFolder">index</base-basic-button>
    </div>
  </div>
</template>

<style scoped>
.input {
    width: auto;
    border: 1px dotted black;
    border-radius: 2px;
    text-align: right; 
    padding: 10px;
}</style>
