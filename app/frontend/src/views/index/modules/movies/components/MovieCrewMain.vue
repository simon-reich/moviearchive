<script setup lang="ts">
import { Departments } from '@/enums/Departments';
import { Director } from '@/enums/JobsDirector';
import { CrewMember } from '@/interfaces/CrewMember';

interface JobData {
    'job': string; 
    'crew': CrewMember[] | null;
}

interface DepartmentData {
  'type': Departments,
  'data': JobData[],
}

interface ComponentProps {
  fullCrew: CrewMember[]
}

const props = defineProps<ComponentProps>();

const departments: DepartmentData[] = [
  { 'type': Departments.Directing, 'data': [] },
  { 'type': Departments.Production, 'data': [] },
  { 'type': Departments.Writing, 'data': [] },
]

const addJobData = (depVar: DepartmentData, department: Departments) => {
  const jobs = Array.from(new Set(props.fullCrew
    .filter((member: CrewMember) => member.department === department)
    .map((member: CrewMember) => member.job)
  ));

  for (const job of jobs) {
    depVar.data.push({
      'job': job,
      'crew': props.fullCrew.filter((member: CrewMember) => member.job === job)
    })
  };
}

onBeforeMount(() => {
  for (const department of departments) {
    addJobData(department, department.type);
  };
});

</script>

<template>
  <div>
      <div v-for="department in departments" :key="department.type">
        <div v-for="(job) in department.data" :key="job.job">
          <div class="subgrid mr-7">
            <index-modules-movies-movie-info-list
              :infoSingular="job.job"
              :infoMultiple="`${job.job}s`"
              :infoKey="'full_crew'"
              :infoValue="job.crew"
              :nextLine="true"
            ></index-modules-movies-movie-info-list>
          </div>
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