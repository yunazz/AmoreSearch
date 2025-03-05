<script setup>
const props = defineProps(["list", "listType"]);
// const emit = defineEmits(["close"]);
</script>

<template>
  <div class="board_cards grid-cols-4">
    <v-card v-for="(item, i) in list" :key="i" class="board_card">
      <div class="card-img">
        <v-img
          height="180px"
          :src="item.image_url"
          cover
          style="border: 1px solid #f1f1f1"
        ></v-img>
      </div>
      <v-card-text class="mt-4 text-clamp-2" style="min-height: 40px">
        <b class="fw-500">{{ item.title }}</b>
      </v-card-text>
      <div class="v-card-custom-action pr-1 pb-1">
        <span class="v-card-date">{{ formatDate(item.created_at) }}</span>
        <v-btn class="icon--toggle" icon="mdi-star" variant="text" />
      </div>
    </v-card>
  </div>
</template>
