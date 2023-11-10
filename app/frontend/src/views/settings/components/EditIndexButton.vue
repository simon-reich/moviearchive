<script setup lang="ts">
import { ref } from 'vue';

interface ComponentProps {
  indexId: string;
  indexName: string;
  modalTitle: string;
}

const props = defineProps<ComponentProps>();
const showModal = ref(false);

const openModal = (indexId: string) => {
    showModal.value = true;
}

const closeModal = (indexId: string) => {
    showModal.value = false;
}
</script>

<template>
    <div @click="openModal(indexId)">
        <i 
            class="iconify text-2xl hover:opacity-20 hover:cursor-pointer"
            data-icon="material-symbols-light:edit-outline-sharp"
        >
        </i>
    </div>

    <base-basic-modal 
        v-if="showModal"
        :modalTitle="modalTitle"
        @close="closeModal"
    >
        <settings-edit-index-content
            :indexId="indexId"
            :indexName="indexName"
            @close="closeModal"
        ></settings-edit-index-content>
    </base-basic-modal>
</template>

<style scoped></style>
