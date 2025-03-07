<script setup>
const props = defineProps({
  list: { required: true },
  scope: { default: false },
  is_favorite: {
    type: Boolean,
    required: false,
  },
});
const emit = defineEmits(["notify", "success"]);

const dialog = ref(false);
const targetItem = ref(null);

function openRnb(item) {
  dialog.value = true;
  targetItem.value = item;
}
function notify(msg) {
  emit("notify", msg);
}
function success() {
  emit("success");
}
</script>

<template>
  <div class="board_cards product_card grid-cols-4">
    <ClientOnly>
      <ListItemProduct
        v-for="item in list"
        :item="item"
        :key="item"
        :scope="scope"
        favorite_type="COSMETIC"
        :is_favorite="is_favorite"
        @notify="notify"
        @success="success"
        @showDetail="openRnb"
      />
      <!-- RNB -->
      <v-navigation-drawer
        class="rnb"
        v-model="dialog"
        temporary
        location="right"
        width="500"
      >
        <template v-if="targetItem">
          <div class="rnb_wrap">
            <div class="rnb_img card-img">
              <v-img height="250" :src="targetItem.image_url" cover></v-img>
            </div>
            <div class="rnb_content">
              <div class="rnb_header ml-3 w-full flex align-center">
                <div class="chip_group">
                  <v-chip
                    v-for="(tag, idx) in targetItem.tags"
                    :key="idx"
                    size="x-small"
                  >
                    {{ tag }}
                  </v-chip>
                  <v-chip size="x-small">{{ targetItem.texture }}</v-chip>
                </div>
                <v-btn
                  icon="mdi-star"
                  variant="text"
                  class="icon--toggle mr-3 mt-2"
                />
              </div>

              <v-card-item class="pt-1">
                <p class="card_title fw-600">
                  {{ targetItem.product_name }}
                </p>
                <v-card-subtitle>
                  <div class="flex px-3 gap-1"></div>
                  <p class="flex gap-2 mt-1">
                    <button class="text-black fw-500 hover_underline">
                      {{ targetItem.brand_kor }}
                    </button>
                    <small>|</small>
                    <span class="body--s">
                      {{ formatNumber(targetItem.price) }}원
                    </span>
                  </p>
                </v-card-subtitle>
              </v-card-item>
              <v-card-text>
                <h4 class="mb-1 fw-600 flex align-center gap-1 word-space--1">
                  <v-icon
                    icon="mdi-information"
                    size="small"
                    color="grey-lighten-1"
                  />
                  ｢화장품법｣에 따라 기재ㆍ표시하여야 하는 모든 성분
                </h4>
                <p>
                  {{ targetItem.ingredients }}
                </p>
              </v-card-text>
              <v-card-text>
                <div>
                  <h4 class="mb-1 fw-600 flex align-center gap-1 word-space--1">
                    <v-icon
                      icon="mdi-information"
                      size="small"
                      color="grey-lighten-1"
                    />
                    ｢화장품법｣에 따른 기능성 화장품 심사(보고) 여부
                  </h4>
                  <p>화장품법에 따른 기능성 화장품 심사를 필함</p>
                </div>
                <div>
                  <h4
                    class="mt-5 mb-1 fw-600 flex align-center gap-1 word-space--1"
                  >
                    <v-icon
                      icon="mdi-information"
                      size="small"
                      color="grey-lighten-1"
                    />
                    제품 주요 사양
                  </h4>
                  <p>제품 주요 사양 안내입니다.</p>
                </div>
                <div>
                  <h4
                    class="mt-5 mb-1 fw-600 flex align-center gap-1 word-space--1"
                  >
                    <v-icon
                      icon="mdi-information"
                      size="small"
                      color="grey-lighten-1"
                    />
                    사용방법
                  </h4>
                  <p>사용방법 안내입니다.</p>
                </div>
                <div>
                  <h4
                    class="mt-5 mb-1 fw-600 flex align-center gap-1 word-space--1"
                  >
                    <v-icon
                      icon="mdi-information"
                      size="small"
                      color="grey-lighten-1"
                    />
                    사용할 때의 주의사항
                  </h4>
                  <p>사용할 때의 주의사항</p>
                </div>
                <div>
                  <h4
                    class="mt-5 mb-1 fw-600 flex align-center gap-1 word-space--1"
                  >
                    <v-icon
                      icon="mdi-information"
                      size="small"
                      color="grey-lighten-1"
                    />
                    사용할 때의 주의사항
                  </h4>
                  <p>
                    1) 화장품 사용 시 또는 사용 후 직사광선에 의하여 사용 부위가
                    붉은 반점, 부어오름 또는 가려움증 등의 이상 증상이나
                    부작용이 있는 경우에는 전문의 등과 상담할 것. 2) 상처가 있는
                    부위 등에는 사용을 자제할 것. 3) 보관 및 취급 시 주의 사항.
                    가) 어린이의 손이 닿지 않는 곳에 보관할 것. 나) 직사광선을
                    피해서 보관할 것
                  </p>
                </div>
                <div>
                  <h4
                    class="mt-5 mb-1 fw-600 flex align-center gap-1 word-space--1"
                  >
                    <v-icon
                      icon="mdi-information"
                      size="small"
                      color="grey-lighten-1"
                    />
                    소비자상담 전화번호
                  </h4>
                  <p>1577-4887</p>
                </div>
              </v-card-text>
            </div>
          </div>
        </template>
      </v-navigation-drawer>
    </ClientOnly>
  </div>
</template>
<style scoped>
h4 {
  font-size: 0.9375rem;
}
.position-absolute {
  position: absolute;
  z-index: 1;
  right: 4px;
  top: 4px;
}
</style>
