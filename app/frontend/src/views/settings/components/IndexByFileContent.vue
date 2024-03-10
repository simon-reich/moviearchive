<script setup lang="ts">
import { UseApiStore } from '@/store/ApiStore';
import { IndexByFileDto } from '@/services/api/dtos/index-by-file.dto';
import { UseIndexStore } from '@/store/IndexStore';

interface ComponentEmits {
  (e: "close"): void;
}

const apiStore = UseApiStore();
const indexStore = UseIndexStore();

const emits = defineEmits<ComponentEmits>();

const indexByFileDto = ref<IndexByFileDto>({
    index_name: await indexStore.getSelectedOrDefault(),
    path: "",
    wikipedia: true,
})

const indexByFile = async () => {
  const response = await apiStore.indexByFile(indexByFileDto.value);
  console.log(response);
  emits('close');
}
</script>

<template>
  <div class="grid grid-cols-2 gap-1">
    <p>file name:</p>
    <base-basic-input class="input" v-model="indexByFileDto.path"></base-basic-input>

    <div file="mt-4">
      <base-basic-button @pressed="indexByFile">index</base-basic-button>
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
