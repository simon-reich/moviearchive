<script setup lang="ts">
import { UseIndexStore } from '@/store/IndexStore';

interface ComponentProps {
  indexName: string;
}

const props = defineProps<ComponentProps>();

const indexStore = UseIndexStore()

const selectIndex = async () => {
    await indexStore.selectIndex(props.indexName)
}
</script>

<template>
    <div @click="selectIndex">
        <div v-if="indexStore.selected?.index === indexName">
            <i
                class="iconify text-2xl hover:opacity-20 hover:cursor-pointer"
                data-icon="material-symbols-light:radio-button-checked-outline"
            ></i>
        </div>
        <div v-else>
            <i
                class="iconify text-2xl hover:opacity-20 hover:cursor-pointer"
                data-icon="material-symbols-light:radio-button-unchecked"
            ></i>
        </div>
    </div>
</template>

<style scoped></style>
