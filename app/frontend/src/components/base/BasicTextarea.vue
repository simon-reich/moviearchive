<template>
    <div>
      <textarea
        class="base-textarea"
        :id="id"
        :value="modelValue"
        @input="updateValue"
        :rows="rows"
        :cols="cols"
        :placeholder="placeholder"
      ></textarea>
    </div>
  </template>
  
  <script setup lang="ts">
  interface ComponentProps {
    id?: string;
    modelValue?: string;
    rows?: number;
    cols?: number;
    placeholder?: string;
  }
  
  interface ComponentEmits {
    (event: "update:modelValue", value: string): void;
  }
  
  const props = defineProps<ComponentProps>();
  const emit = defineEmits<ComponentEmits>();
  
  const updateValue = (event: Event) => {
    const target = event.target as HTMLTextAreaElement;
    emit("update:modelValue", target.value);
  };
  </script>
  
  <style scoped>
  .base-textarea {
    /* Add your custom styles here */
    width: 100%;
    height: 200px; /* Adjust the initial height as needed */
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    background-color: #fff;
    color: #333;
    font-size: 16px;
  }
  
  .base-textarea::placeholder {
    color: #999; /* Adjust placeholder text color */
  }
  </style>
  