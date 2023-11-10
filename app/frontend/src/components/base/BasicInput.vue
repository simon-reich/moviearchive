<script setup lang="ts">
interface ComponentProps {
  id?: string;
  type?: string;
  defaultValue?: string;
  modelValue?: string | number;
}

interface ComponentEmits {
  (event: "update:modelValue", value: string): void;
}

const props = withDefaults(defineProps<ComponentProps>(), {
  id: "",
  type: "text",
  modelValue: "",
});
const emit = defineEmits<ComponentEmits>();

const updateValue = (event: Event) => {
  const target = event.target as HTMLInputElement;
  emit("update:modelValue", target.value);
};
</script>

<template>
  <input
    class=""
    :id="id"
    :type="type"
    :value="modelValue"
    @input="updateValue"
  />
</template>

<style scoped></style>
