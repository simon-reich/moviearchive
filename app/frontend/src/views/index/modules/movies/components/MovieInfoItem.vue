<script setup lang="ts">

interface ComponentProps {
  info: string;
  infoValue?: string | number | null;
  infoKey?: string;
  link?: string;
  textStyling?: string;
}

const props = defineProps<ComponentProps>();

</script>

<template>
    <div>
        <p class="font-semibold">{{ info }}</p>
    </div>
    <a v-if="link" class="hover:opacity-20" :href="link">
        <p :class="textStyling">{{ infoValue }}</p>
    </a>
    <base-index-link
        v-else-if="infoKey"
        :field="infoKey"
        :value="infoValue"
        :searchOption="'exact'"
        >
    </base-index-link>
    <p v-else :class="textStyling">{{ infoValue }}</p>
</template>

<style scoped lang="postcss">
</style>