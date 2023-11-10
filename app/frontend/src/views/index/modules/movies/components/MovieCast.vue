<script setup lang="ts">
import { CastMember } from '@/interfaces/CastMember';

interface ComponentProps {
  fullCast: CastMember[]
}

const props = defineProps<ComponentProps>();

const cast = props.fullCast.sort((a, b) => a.order - b.order);

</script>

<template>
  <div>
      <div v-for="member in cast" :key="member.id">
        <div class="subgrid mr-7">
            <index-modules-movies-movie-info-item
                :info="member.character"
                :infoValue="member.name"
                :infoKey="'full_cast'"
            ></index-modules-movies-movie-info-item>
        </div>
      </div>
    </div>
</template>

<style scoped lang="postcss">
.subgrid {
    display: grid;
    gap: 0.2em;
    grid-template-columns: 2fr 2fr;
}
</style>