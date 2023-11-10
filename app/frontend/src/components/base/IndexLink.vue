<script setup lang="ts">
import { BasicQuery } from "@/interfaces/BasicQuery";
import { router } from "@/routes";
import { UseIndexSearchStore } from "@/store/IndexSearchStore";

interface ComponentProps {
  field: string;
  value: string;
  searchOption: string;
}

const indexSearchStore = UseIndexSearchStore();

const props = defineProps<ComponentProps>();

const clicked = async () => {
  const query: BasicQuery = {
    field: props.field,
    value: props.value,
    size: 1000,
  };
  if (props.searchOption === "exact") {
    await indexSearchStore.getExactResults(query);
  } else if (props.searchOption === "singleField") {
    await indexSearchStore.getMatchResults(query);
  } else if (props.searchOption === "multiField") {
    await indexSearchStore.getMultiMatchResults(query);
  }
  router.push({ name: "index.search" });
};
</script>

<template>
  <span class="hover:opacity-20 hover:cursor-pointer" @click="clicked">
    {{ value }}
  </span>
  <slot></slot>
</template>

<style scoped></style>
