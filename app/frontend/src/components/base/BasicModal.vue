<script setup lang="ts">
    interface ComponentProps {
        modalTitle: string;
    }

    interface ComponentEmits {
        (e: "close"): void;
    }

    const props = defineProps<ComponentProps>();
    const emits = defineEmits<ComponentEmits>();

    const closeModal = () => {
        emits("close");
    };
</script>

<template>
    <div class="modal" @click="closeModal">
      <div class="modal-dialog" @click.stop="">
        <div class="modal-content">
          <div class="modal-header">
            <h2>{{ modalTitle }}</h2>
            <button @click="closeModal">Close</button>
          </div>
          <div class="modal-body">
            <slot></slot>
          </div>
        </div>
      </div>
    </div>
</template>

<style scoped>
    /* Add your modal styles here */
    .modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 999;
    }

    .modal-dialog {
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
    width: 80%;
    max-width: 400px;
    }

    .modal-content {
    padding: 16px;
    }

    .modal-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #ccc;
    padding: 16px;
    }

    .modal-header h2 {
    margin: 0;
    }

    .modal-body {
    padding: 16px;
    }

    button {
    background: none;
    border: none;
    cursor: pointer;
    font-weight: bold;
    color: #0077b5;
    }
</style>
