<script setup>
const props = defineProps({
  item: { required: true },
  scope: { required: true },
  favorite_type: { type: String },
  is_favorite: {
    type: Boolean,
    required: false,
  },
});
const emit = defineEmits(["showDetail", "notify", "success"]);

const is_favorite = ref(props.is_favorite || !isEmpty(props.item?.is_favorite));

const product = ref({
  scope: props.scope || props.item.scope,
  cosmetic_id: props.item.cosmetic_id || props.item.external_cosmetic_id,
  category_1: props.item.category_1 || props.item.external_category_1,
  category_2: props.item.category_2 || props.item.external_category_2,
  product_name: props.item.product_name || props.item.external_product_name,
  product_info: props.item.product_info || props.item.external_product_info,
  capacity: props.item.capacity || props.item.external_capacity,
  specification: props.item.specification || props.item.external_specification,
  expiration_date:
    props.item.expiration_date || props.item.external_expiration_date,
  use_period: props.item.use_period || props.item.external_use_period,
  ingredients: props.item.ingredients || props.item.external_ingredients,
  precaution: props.item.precaution || props.item.external_precaution,
  price: props.item.price || props.item.external_price,
  manufacture: props.item.manufacture || props.item.external_manufacture,
  quality_standards:
    props.item.quality_standards || props.item.external_quality_standards,
  mfds: props.item.mfds || props.item.external_mfds,
  image_url: props.item.image_url || props.item.external_image_url,
  brand_kor: props.item.brand_kor || props.item.external_brand_kor,
  is_favorite: is_favorite.value,
});

function openRnb(item) {
  emit("showDetail", item);
}
async function toggleFavorites() {
  const body = {
    favorite_type: "COSMETIC",
    target_id: product.value.cosmetic_id,
    scope: props.scope || product.value.scope,
  };

  let method = "";
  if (is_favorite.value) method = "DELETE";
  if (!is_favorite.value) method = "POST";

  try {
    const { code, msg } = await $http("/member/favorites", {
      method,
      body,
    });

    emit("notify", msg);
    emit("success");
    if (code == 0) {
      is_favorite.value = !is_favorite.value;
      product.value.is_favorite = !product.value.is_favorite;
    }
  } catch (e) {
    emit("notify", "서버 오류 발생");
  }
}
</script>

<template>
  <ClientOnly>
    <v-card>
      <div class="card-img">
        <v-img
          height="250"
          :src="product.image_url"
          cover
          class="detail_img cur-p"
          @click="openRnb(product)"
        ></v-img>
      </div>
      <v-card-item>
        <p class="card_title text-clamp-2 fw-500">
          {{ product.product_name }}
        </p>
        <v-card-subtitle>
          <p class="flex gap-2 mt-1">
            <button class="text-black fw-500 hover_underline">
              {{ product.brand_kor }}
            </button>
            <small>|</small>
            <span class="body--s"> {{ formatNumber(product.price) }}원 </span>
          </p>
        </v-card-subtitle>
      </v-card-item>
      <v-card-text class="pb-2">
        <p class="text-clamp-6">{{ product.ingredients }}</p>
      </v-card-text>
      <div class="w-full flex justify-between align-center">
        <div class="flex px-3 gap-1">
          <!-- <v-chip v-for="(tag, idx) in product.tags" :key="idx" size="small">
            {{ tag }}
          </v-chip>
          <v-chip size="small">{{ product.texture }}</v-chip> -->
        </div>
        <div>
          <v-btn
            icon="mdi-star"
            variant="text"
            class="icon--toggle mb-1 mr-1"
            :class="{ active: is_favorite }"
            @click="toggleFavorites()"
          />
        </div>
      </div>
    </v-card>
  </ClientOnly>
</template>
<style scoped>
.detail_img {
  border-radius: 12px;
}
.detail_img:after {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: rgba(0, 0, 0, 0.524);
  font-family: "Material Design Icons" !important;
  content: "\F0349";
  font-size: 40px;
  color: white;
  pointer-events: none;
  opacity: 0;
  z-index: 0;
  transition: all 0.2s ease;
}
.detail_img:hover:after {
  display: flex;
  pointer-events: initial;
  z-index: 1;
  opacity: 1;
}
</style>
