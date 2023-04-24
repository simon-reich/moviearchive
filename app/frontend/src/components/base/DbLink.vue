<script setup lang="ts">
import { BasicQuery } from "@/interfaces/BasicQuery";
import { router } from "@/routes";
import { useSearchResultsStore } from "@/store/searchResults";

interface ComponentProps {
  field: string;
  value: string;
  searchOption: string;
}

const searchResultsStore = useSearchResultsStore();

const props = defineProps<ComponentProps>();

const clicked = async () => {
  const query: BasicQuery = {
    field: props.field,
    value: props.value,
    size: 1000,
  };
  if (props.searchOption === "exact") {
    searchResultsStore.getExactResults(query);
  } else if (props.searchOption === "singleField") {
    searchResultsStore.getMatchResults(query);
  } else if (props.searchOption === "multiField") {
    searchResultsStore.getMultiMatchResults(query);
  }
  router.push({ name: "database.search" });
};
</script>

<template>
  <span class="hover:opacity-20 hover:cursor-pointer" @click="clicked">
    {{ value }}
  </span>
  <slot></slot>
</template>

<style scoped></style>
