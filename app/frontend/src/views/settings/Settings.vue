<script setup lang="ts">
import { DatabaseService } from '@/services/database/DatabaseService';
import { IndexFolderDto } from '@/services/database/dtos/index-folder.dto'

const folderPathToIndex = ref<IndexFolderDto>({
    path: "",
})

const createIndex = async () => {
    const response = await DatabaseService.createIndex();
    if(response) {
        console.log(response)
    }
};

const getIndicies = async () => {
    const response = await DatabaseService.getAllIndicies();
    if(response) {
        console.log(response)
    }
};

const indexFolder = async () => {
    const response = await DatabaseService.indexFolder();
    if(response) {
        console.log(response)
    }
}
</script>

<template>
    <p>Settings</p>
    <div class="m-5">
        <router-link :to="{ name: 'home' }">home</router-link>
    </div>
    <div>
        <p class="font-light italic pt-2 pl-1">
            <span
                class="hover:cursor-pointer hover:opacity-20"
                @click="createIndex"
            >
                create index
            </span>
        </p>
    </div>
    <div>
        <p class="font-light italic pt-2 pl-1">
            <span
                class="hover:cursor-pointer hover:opacity-20"
                @click="getIndicies"
            >
                get indicies
            </span>
        </p>
    </div>
    <div>
        <p class="font-light italic pt-2 pl-1">
            <span
                class="hover:cursor-pointer hover:opacity-20"
                @click="indexFolder"
            >
                index folder
            </span>
        </p>
    </div>
</template>

<style lang="postcss" scoped></style>
