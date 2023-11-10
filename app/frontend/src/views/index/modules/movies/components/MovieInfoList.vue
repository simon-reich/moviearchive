<script setup lang="ts">

interface ComponentProps {
  infoSingular: string;
  infoMultiple?: string;
  infoKey?: string;
  infoValue?: string[] | number[] | { [key: string] : any }[] | null;
  nextLine?: boolean;
}

const props = defineProps<ComponentProps>();

const computedInfoValue = computed(() => {
  return props.infoValue ? props.infoValue.map(value => {
    if (typeof value === 'string' || typeof value === 'number') {
      return value.toString();
    } else {
      return value.name;
    }
  }) : null;
});
</script>

<template>
    <div class="font-semibold">
        <p v-if="infoValue && infoValue.length === 1">
          {{ infoSingular }}
        </p>
        <p v-if="infoValue && infoValue.length > 1">
          {{ infoMultiple }}
        </p>
      </div>

      <div v-if="nextLine">
        <span v-for="(value, index) in computedInfoValue" :key="value">
          <div>
            <base-index-link
              :field="infoKey"
              :value="value"
              :searchOption="'exact'"
            >
              <span
                v-if="
                  infoValue && 
                  infoValue.length > 1 &&
                  index < infoValue.length - 1"
                >,
              </span>
            </base-index-link>
          </div>
        </span>
      </div>
      
      <div v-else>
        <span v-for="(value, index) in computedInfoValue" :key="value">
          <base-index-link
            :field="infoKey"
            :value="value"
            :searchOption="'exact'"
          >
            <span
              v-if="
                infoValue && 
                infoValue.length > 1 &&
                index < infoValue.length - 1"
              >,
            </span>
          </base-index-link>
        </span>
      </div>
</template>

<style scoped lang="postcss">
</style>