<script setup>
const tabs = ref([
  { text: "뉴스/저널", value: "EXTERNAL_POST" },
  { text: "화장품", value: "COSMETIC" },
  { text: "회사뉴스", value: "INTERNAL_NEWS" },
  { text: "사내문서", value: "INTERNAL_DOCS" },
]);
const snackbar = ref({ active: false, message: "" });
const favorite_type = ref({ text: "뉴스/저널", value: "NEWS_JOURNAL" });

const dialog = ref(false);

const filter = ref({
  favorite_type: "EXTERNAL_POST",
  query: "",
  current_page: 1,
  item_per_page: 20,
});

const filter_query = computed(() => ({
  favorite_type: filter.value.favorite_type,
  query: filter.value.query,
  current_page: filter.value.current_page,
  item_per_page: filter.value.item_per_page,
}));

const {
  data: board,
  status,
  refresh,
} = useApi("/member/favorites", {
  key: "favorites-board",
  query: filter_query,
});
const total_cnt = computed(() => board.value.paging.total_rows);

function openRnb(item) {
  dialog.value = true;
  targetItem.value = item;
}

function changePage(current_page) {
  if (current_page === filter.value.current_page) {
    return;
  }
  filter.value.current_page = current_page;
  scrollToTop();
}

function notify(msg) {
  snackbar.value.active = true;
  snackbar.value.message = msg;
}

watch(favorite_type, (newValue) => {
  filter.value.favorite_type = newValue.value;
  changePage(1);
});
</script>

<template>
  <div id="Favorites" class="content">
    <div class="content_inner">
      <ClientOnly>
        <div class="page_header">
          <h2 class="page_title">즐겨찾기</h2>
          <div class="board_tab depth-1">
            <v-tabs
              v-model="favorite_type"
              bg-color="transparent"
              align-tabs="center"
              density="comfortable"
              selected-class="text-primary"
            >
              <v-tab
                v-for="tab in tabs"
                :key="tab.value"
                :text="tab.text"
                :value="tab"
                :ripple="false"
              />
            </v-tabs>
          </div>
        </div>
        <div class="board">
          <div class="board_content">
            <template v-if="filter.favorite_type == 'EXTERNAL_POST'">
              <ListItemLink
                v-for="item in board?.result"
                :key="item?.target_id"
                :item="item"
                :is_favorite="true"
                scope="EXTERNAL"
                @notify="notify"
                @success="refresh"
              />
            </template>

            <template v-else-if="filter.favorite_type == 'COSMETIC'">
              <ListProduct :list="board?.result" />
            </template>

            <template v-else-if="filter.favorite_type == 'INTERNAL_NEWS'">
              <div v-if="board?.result" class="board_cards grid-cols-4">
                <ListItemNews
                  v-for="item in board?.result"
                  :key="item?.target_id"
                  :item="item"
                  :is_favorite="true"
                  scope="INTERNAL"
                  @notify="notify"
                  @success="refresh"
                />
              </div>
            </template>

            <template v-else-if="filter.favorite_type == 'INTERNAL_DOCS'">
              <ListItemLink
                v-for="(item, index) in board?.result"
                :key="index"
                :is_favorite="true"
                :item="item"
                scope="INTERNAL"
                @notify="notify"
                @success="refresh"
              />
            </template>
          </div>

          <Paging
            no-content-text="등록된 즐겨찾기가 없습니다."
            no-content-icon="mdi-star-off"
            :paging="filter"
            :status="status"
            :total_row="total_cnt"
            @changePage="changePage"
          />
        </div>
        <v-snackbar v-model="snackbar.active" :timeout="1000" color="primary">
          {{ snackbar.message }}
        </v-snackbar>
      </ClientOnly>
    </div>
  </div>
</template>

<style scoped>
.rnb_header {
  height: 38px;
  margin-left: 0.75rem;
  width: 100%;
  display: flex;
  align-items: center;
}
.chip_group {
  width: 100%;
  display: flex;
  align-items: center;
  grid-template: 4rem;
  margin-top: 10px;
}
</style>
