<script setup lang="ts">
interface ComponentEmits {
  (e: "pressed"): void;
}

const emits = defineEmits<ComponentEmits>();

const buttonClick = () => {
  emits("pressed");
};
</script>

<template>
  <button
    class="border-1 border-black bg-gray-400 hover:bg-gray-300 p-1"
    @click="buttonClick"
  >
    <slot></slot>
  </button>
</template>

<style lang="postcss" scoped></style>
