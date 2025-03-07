<script setup>
const props = defineProps(["item", "loading"]);
async function addFavorites() {
  const body = {
    favorite_type: item.favorite_type,
    target_id: item.target_id,
    source: item.source,
  };
  const { code, msg } = await $http("/member/favorites", {
    method: "POST",
    body,
  });

  console.log(code);
  console.log(msg);
}
</script>

<template>
  <v-card class="board_card">
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
      <v-btn
        class="icon--toggle"
        icon="mdi-star"
        variant="text"
        @click="addFavorites"
      />
    </div>
  </v-card>
</template>
