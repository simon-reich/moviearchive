<script setup lang="ts">
</script>

<template>
    <div class="message">
        <slot></slot>
    </div>
</template>

<style scoped>
.message {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: black;
    color: white;
    padding: 15px;
    border-radius: 5px;
    z-index: 1000;
    animation: slideIn 0.5s ease-in-out, fadeOut 0.5s 2s ease-in-out forwards;
  }
  
  @keyframes slideIn {
    from {
      transform: translateX(100%);
    }
    to {
      transform: translateX(0);
    }
  }
  
  @keyframes fadeOut {
    from {
      opacity: 1;
    }
    to {
      opacity: 0;
    }
  }
</style>