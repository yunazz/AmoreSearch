<script setup>
const props = defineProps(["list", "listType"]);
// const emit = defineEmits(["close"]);
</script>

<template>
  <v-list :items="list" lines="two" item-props>
    <template v-slot:subtitle="{ subtitle }">
      <div v-html="subtitle" class="mr-8"></div>
    </template>
    <template v-slot:append>
      <NuxtLink external>
        <v-btn color="grey-lighten-1" icon="mdi-link" variant="text" />
      </NuxtLink>
      <v-btn class="icon--toggle" icon="mdi-star" variant="text" />
    </template>
  </v-list>
</template>
