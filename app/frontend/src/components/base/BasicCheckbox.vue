<script setup lang="ts">
  interface ComponentProps {
    modelValue?: boolean;
  }
  
  interface ComponentEmits {
    (event: "update:modelValue", value: boolean): void;
  }
  
  const props = withDefaults(defineProps<ComponentProps>(), {
    modelValue: false,
  });
  
  const emit = defineEmits<ComponentEmits>();
  
  const updateValue = () => {
    emit("update:modelValue", !props.   modelValue);
  };
</script>

<template>
    <div>
      <input
        class="block p-1 bg-dark-800 text-light-50"
        type="checkbox"
        :checked="modelValue"
        @change="updateValue"
      />
    </div>
</template>
  
<style scoped></style>
  