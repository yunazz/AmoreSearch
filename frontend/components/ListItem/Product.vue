<script setup>
import { ClientOnly } from "#components";

const props = defineProps(["item"]);
const emit = defineEmits(["showDetail"]);

const dialog = ref(false);
const targetItem = ref(null);

function openRnb(item) {
  emit("showDetail", item);
}
</script>

<template>
  <ClientOnly>
    <v-card>
      <v-btn
        icon="mdi-star"
        variant="text"
        class="icon--toggle position-absolute"
      />
      <div class="card-img">
        <v-img height="250" :src="item.image_url" cover></v-img>
      </div>
      <v-card-item>
        <p class="card_title text-clamp-2">
          {{ item.product_name }}
        </p>
        <v-card-subtitle>
          <p class="flex gap-2 mt-1">
            <button class="text-black fw-500 hover_underline">
              {{ item.brand_kor }}
            </button>
            <small>|</small>
            <span class="body--s"> {{ formatNumber(item.price) }}원 </span>
          </p>
        </v-card-subtitle>
      </v-card-item>
      <v-card-text lines="">
        <p class="text-clamp-6">{{ item.ingredients }}</p>
      </v-card-text>
      <div class="w-full flex justify-between align-center">
        <div class="flex px-3 gap-1">
          <v-chip v-for="(tag, idx) in item.tags" :key="idx" size="small">
            {{ tag }}
          </v-chip>
          <v-chip size="small">{{ item.texture }}</v-chip>
        </div>

        <v-btn
          icon="mdi-chevron-right"
          variant="text"
          class="mr-1 mb-2"
          @click="openRnb(item)"
        />
      </div>
    </v-card>
  </ClientOnly>
</template>
<style scoped>
.position-absolute {
  position: absolute;
  z-index: 1;
  right: 4px;
  top: 4px;
}
</style>
