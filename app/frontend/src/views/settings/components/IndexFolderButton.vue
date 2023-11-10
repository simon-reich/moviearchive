<script setup lang="ts">
import { ref } from 'vue';

interface ComponentProps {
  modalTitle: string;
}

const props = defineProps<ComponentProps>();
const showModal = ref(false);

const openModal = () => {
    showModal.value = true;
}

const closeModal = () => {
    showModal.value = false;
}
</script>

<template>
    <base-basic-button @pressed="openModal()" class="w-50">
        {{ modalTitle }}
    </base-basic-button>

    <base-basic-modal 
        v-if="showModal"
        :modalTitle="modalTitle"
        @close="closeModal"
    >
        <settings-index-folder-content
            @close="closeModal"
        ></settings-index-folder-content>
    </base-basic-modal>
</template>

<style scoped></style>
