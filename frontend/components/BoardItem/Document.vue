<script setup>
const props = defineProps(["list", "listType"]);
// const emit = defineEmits(["close"]);
</script>

<template>
  <v-list :items="list" lines="two" item-props>
    <template v-slot:subtitle="{ subtitle }">
      <div v-html="subtitle" class="mr-10"></div>
    </template>
    <template v-slot:append>
      <v-btn color="grey-lighten-2" icon="mdi-folder" variant="text" />
      <v-btn
        class="icon--favorite"
        color="grey-lighten-2"
        icon="mdi-star"
        variant="text"
      />
    </template>
  </v-list>
</template>
