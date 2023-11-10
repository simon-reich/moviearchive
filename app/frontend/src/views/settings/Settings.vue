<script setup lang="ts">
import { router } from '@/routes';
import { UseIndexStore } from '@/store/IndexStore';

const indexStore = UseIndexStore();

const getBack = () => {
    router.push({ name: "index.search" });
}

onBeforeMount(async () => {
    await indexStore.getIndicies();
});
</script>

<template>
    <h1 class="mx-80 my-20 font-extrabold text-5xl">Settings</h1>

    <div class="grid grid-cols-2 gap-1 mx-80">

        <!-- FUNCTION BUTTONS -->
        <div class="flex flex-col items-start">
            <div class="flex flex-col w-full items-start gap-2">
                <base-basic-button
                    class="w-50" 
                    @pressed="getBack"
                >
                    back
                </base-basic-button>

                <settings-create-index-button :modalTitle="'create index'"></settings-create-index-button>
                
                <settings-index-folder-button :modalTitle="'index folder'"></settings-index-folder-button>
            </div>
        </div>

        <!-- INDICES INFO -->
        <div>
            <div class="grid grid-cols-6 gap-1 mb-5">
                <p class="flex flex-col items-end font-extrabold">index</p>
                <p class="flex flex-col items-end font-extrabold">docs</p>
                <p class="flex flex-col items-end font-extrabold">docs deleted</p>
                <p class="flex flex-col items-end font-extrabold">health</p>
                <p class="flex flex-col items-end font-extrabold">size</p>
                <p class="flex flex-col items-end font-extrabold">action</p>
            </div>
            <div v-for="index in indexStore.indices" :key="index.index">
                <div class="grid grid-cols-6 gap-1">
                    <p class="flex flex-col items-end">{{ index.index }}</p>
                    <p class="flex flex-col items-end">{{ index.docs_count }}</p>
                    <p class="flex flex-col items-end">{{ index.docs_deleted }}</p>
                    <div class="flex flex-col items-end">
                        <div
                            :class="{
                                'green-dot': index.health === 'green', 
                                'yellow-dot': index.health === 'yellow', 
                                'red-dot': index.health === 'red'
                            }"
                        ></div>
                    </div>
                    <p class="flex flex-col items-end">{{ index.store_size }}</p>
                    <div class="flex flex-row w-full justify-end">
                        <settings-delete-index-button
                            :indexName="index.index"
                        ></settings-delete-index-button>
                        <settings-select-index-button
                            :indexName="index.index"
                        ></settings-select-index-button>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
</template>

<style lang="postcss" scoped>
.green-dot {
    width: 10px; 
    height: 10px;
    background-color: green;
    border-radius: 50%;
}

.yellow-dot {
    width: 10px;
    height: 10px;
    background-color: yellow;
    border-radius: 50%;
}

.red-dot {
    width: 10px;
    height: 10px;
    background-color: red;
    border-radius: 50%;
}
</style>
