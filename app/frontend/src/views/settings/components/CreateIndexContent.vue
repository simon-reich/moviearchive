<script setup lang="ts">
import { UseIndexStore } from '@/store/IndexStore';
import { Schemas } from '@/enums/Schemas';
import { CreateIndexDto } from '@/services/index/dtos/create-index.dto';
import { DatabaseService } from "@/services/database/DatabaseService";

interface ComponentEmits {
  (e: "close"): void;
}

const indexStore = UseIndexStore()

const emits = defineEmits<ComponentEmits>();

const schemaOptions = Object.values(Schemas) as string[];

const createIndexDto = ref<CreateIndexDto>({
    name: null,
    schema: null,
})

const createIndex = async () => {
  const response_index = await indexStore.createIndex(createIndexDto.value)
  const response_db = await DatabaseService.createIndex(createIndexDto.value)
  console.log(`${response_index} ${response_db}`);
  emits('close');
}
</script>

<template>
  <div class="grid grid-cols-2 gap-1">
    <p>index name:</p>
    <base-basic-input class="input" v-model="createIndexDto.name"></base-basic-input>

    <p>select schema:</p>
    <base-basic-select 
        v-model="createIndexDto.schema" 
        :items="schemaOptions"
    ></base-basic-select>

    <div class="mt-4">
      <base-basic-button @pressed="createIndex">create</base-basic-button>
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
