<script setup lang="ts">
type Item = Record<string, unknown>;

interface ComponentProps {
  modelValue: string | number;
  items: Item[] | string[] | number[];
  defaultValue?: string;
}

interface ComponentEmits {
  (event: "update:modelValue", value: string | number): void;
}

const props = withDefaults(defineProps<ComponentProps>(), {
  defaultValue: "select",
});
const emit = defineEmits<ComponentEmits>();

const emitSelection = (event: Event) => {
  const target = event.target as HTMLInputElement;
  emit("update:modelValue", target.value);
};
</script>

<template>
  <div>
    <select
      class="select-frame bg-dark-800 hover:bg-dark-200"
      :value="modelValue"
      @change="emitSelection"
    >
      <slot name="headerOption"></slot>
      <option value="" disabled>{{ defaultValue }}</option>
      <option
        v-for="(item, index) in items"
        :key="index"
        :value="item"
        :selected="item === modelValue"
      >
        {{ item }}
      </option>
    </select>
  </div>
</template>

<style scoped>
.select-frame {
  border-bottom: 1px solid white;
  border-right: 1px solid white;
}
</style>
