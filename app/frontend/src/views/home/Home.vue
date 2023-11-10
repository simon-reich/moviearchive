<script setup lang="ts">
import { UseIndexStore } from '@/store/IndexStore';

const indexStore = UseIndexStore();
indexStore.initialize();

</script>

<template>
  <div class="flex flex-col h-full justify-center items-center">
    <div class="hover:opacity-20 text-10xl font-extrabold mr-100 mb-[-60px]">
      <router-link :to="{ name: 'api' }">save movie</router-link>
    </div>
    <div class="hover:opacity-20  text-10xl font-extrabold ml-10 flip">
      <router-link :to="{ name: 'index' }">search movie</router-link>
    </div>
  </div>
</template>

<style scoped>

.flip {
  transform: scaleX(-1) scaleY(-1);
  filter: FlipH; 
}

.gap-reduce {
  margin-bottom: -30px;
}
</style>
