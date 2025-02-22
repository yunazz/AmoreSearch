<script setup>
const props = defineProps(["list", "listType"]);
// const emit = defineEmits(["close"]);
</script>

<template>
  <div class="board_cards grid-cols-4">
    <v-card v-for="(item, i) in list" :key="i" class="board_card">
      <div class="card-img">
        <v-img height="180px" :src="item.img_url" cover></v-img>
      </div>
      <v-card-title class="my-2"> {{ item.title }} </v-card-title>
      <v-card-subtitle> {{ item.subtitle }} </v-card-subtitle>
      <v-card-text> {{ item.text }} </v-card-text>

      <div class="v-card-custom-action pr-1 pb-1">
        <span class="v-card-date">{{ item.registered_at }}</span>
        <v-btn
          class="icon--favorite"
          color="grey-lighten-2"
          icon="mdi-star"
          variant="text"
        />
      </div>
    </v-card>
  </div>
</template>
