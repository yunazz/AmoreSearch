<script setup>
const props = defineProps(["dialog", "propItem"]);
const emit = defineEmits(["close"]);
const isActive = ref(props.dialog);

function closeDialog() {
  emit("close");
}
</script>
<template>
  <div>
    <v-navigation-drawer
      v-model="isActive"
      temporary
      location="right"
      width="400"
      @update:modelValue="closeDialog"
    >
      <v-card class="board_card">
        <template v-slot:loader="{ isActive }">
          <v-progress-linear
            :active="isActive"
            color="deep-purple"
            height="4"
            indeterminate
          ></v-progress-linear>
        </template>
        <div class="card-img">
          <v-img
            height="250"
            src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
            cover
          ></v-img>
        </div>
        <v-card-item>
          <v-card-title>화장품명</v-card-title>
          <v-card-subtitle>
            <p class="flex gap-2">
              브랜드
              <small>|</small>
              가격
            </p>
          </v-card-subtitle>
        </v-card-item>
        <v-card-text>
          <div>성분1, 성분2, 성분3, 성분4</div>
          <div class="text-subtitle-2 text-gray-05"></div>
        </v-card-text>
      </v-card>
    </v-navigation-drawer>
  </div>
</template>
