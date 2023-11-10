<script setup lang="ts">
import { onBeforeMount, ref } from 'vue';
import { UseIndexStore } from '@/store/IndexStore';
import { EditIndexDto } from '@/services/index/dtos/edit-index.dto';

interface ComponentProps {
  indexId: string;
  indexName: string;
}

interface ComponentEmits {
  (e: "close"): void;
}

const IndexStore = UseIndexStore()

const props = defineProps<ComponentProps>();
const emits = defineEmits<ComponentEmits>();

const indexEditValues = ref<EditIndexDto>({
    uuid: props.indexId,
    index: props.indexName,
})

const editIndex = async () => {
  emits('close');
}

onBeforeMount(async () => { });
</script>

<template>
  <div class="grid grid-cols-2 gap-1">
    <p>index name:</p>
    <base-basic-input class="input" v-model="indexEditValues.index"></base-basic-input>

    <div class="mt-4">
      <base-basic-button @pressed="editIndex">edit</base-basic-button>
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
}

</style>
