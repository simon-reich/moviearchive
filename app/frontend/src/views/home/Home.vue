<script setup lang="ts"></script>

<template>
  <div class="flex flex-row justify-around h-full items-center">
    <div class="hover:opacity-20">
      <router-link :to="{ name: 'archive' }">archive</router-link>
    </div>
    <div class="hover:opacity-20">
      <router-link :to="{ name: 'database' }">database</router-link>
    </div>
  </div>
</template>

<style scoped></style>
