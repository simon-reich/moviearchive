<script setup lang="ts">
interface ComponentProps {
  title: string;
  docId: string;
  imdbId: string;
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
            data-icon="material-symbols-light:edit-outline-sharp"
        >
        </i>
    </div>

    <base-basic-modal 
        v-if="showModal"
        :modalTitle="`edit ${title}`"
        @close="closeModal"
    >
        <index-modules-search-search-result-edit-content 
            :docId="docId"
            :imdbId="imdbId"
            @close="closeModal"
        ></index-modules-search-search-result-edit-content>
    </base-basic-modal>
</template>

<style scoped></style>
