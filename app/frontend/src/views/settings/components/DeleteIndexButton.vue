<script setup lang="ts">

interface ComponentProps {
    indexName: string;
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
    <div @click="openModal()">
        <i 
            class="iconify text-2xl hover:opacity-20 hover:cursor-pointer"
            data-icon="material-symbols-light:delete-outline-sharp"
        >
        </i>
    </div>

    <base-basic-modal 
        v-if="showModal"
        :modalTitle="`delete ${indexName}`"
        @close="closeModal"
    >
        <settings-delete-index-content
            :indexName="indexName"
            @close="closeModal"
        ></settings-delete-index-content>
    </base-basic-modal>
</template>

<style scoped></style>
