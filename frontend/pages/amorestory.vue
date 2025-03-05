<script setup>
const config = useRuntimeConfig().public;
const tabs = [
  { text: "회사뉴스", value: "NEWS" },
  { text: "IR 및 기타 보고서", value: "REPORT" },
  { text: "브랜드", value: "BRAND" },
  // { text: "사내문서", value: "DOCUMENT" },
];

const post_type = ref({ text: "회사뉴스", value: "NEWS" });
const post_ctgry = ref({ name: "전체", value: "" });

const filter = ref({
  post_type: "NEWS",
  post_ctgry: "",
  current_page: 1,
  item_per_page: 8,
});

const filter_query = computed(() => ({
  post_type: filter.value.post_type,
  post_ctgry: filter.value.post_ctgry,
  current_page: filter.value.current_page,
  item_per_page: filter.value.item_per_page,
}));

function changePage(current_page) {
  console.log(current_page);
  if (current_page === filter.value.current_page) {
    return;
  }
  filter.value.current_page = current_page;
  scrollToTop();
}

const { data: board, status } = useApi("/amorestory/board", {
  key: "amorestory-board",
  query: filter_query,
});

const total_cnt = computed(() => board.value.paging.total_rows);

watch(post_type, (newValue) => {
  filter.value.post_type = newValue.value;
  filter.value.post_ctgry = "";
  post_ctgry.value = { name: "전체", value: "" };
  filter.value.current_page = 1;
  if (newValue.value === "NEWS") filter.value.item_per_page = 8;
  else if (newValue.value === "REPORT") filter.value.item_per_page = 20;
  else if (newValue.value === "BRAND") filter.value.item_per_page = 100;
});

watch(post_ctgry, (newValue) => {
  filter.value.post_ctgry = newValue.value;
  filter.value.current_page = 1;
});
</script>

<template>
  <div id="AmoreStory" class="content">
    <div class="content_inner">
      <div class="page_header">
        <h2 class="page_title">아모레스토리</h2>
        <div class="board_tab depth-1">
          <ClientOnly>
            <v-tabs
              v-model="post_type"
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
          </ClientOnly>
        </div>
        <div class="board_tab depth-2">
          <ClientOnly>
            <v-btn-toggle v-model="post_ctgry" mandatory rounded="0">
              <v-btn
                v-for="(board, index) in boardCategory[post_type.value]"
                :key="index"
                :value="board"
                :ripple="false"
                height="40"
                min-width="72"
                selected-class="text-primary"
              >
                {{ board.name }}
              </v-btn>
            </v-btn-toggle>
          </ClientOnly>
        </div>
      </div>
      <template v-if="status === 'success'">
        <div class="board">
          <div class="board_content">
            <!-- 회사뉴스 -->
            <template v-if="post_type.value === 'NEWS'">
              <div class="board_cards grid-cols-4">
                <CardNews
                  v-for="(item, i) in board?.result"
                  :key="i"
                  :item="item"
                  :loading="true"
                />
              </div>
            </template>

            <!-- 보고서 -->
            <template v-else-if="post_type.value === 'REPORT'">
              <ListDocument
                v-if="post_type.value === 'REPORT'"
                :list="board?.result"
              />
            </template>

            <!-- 브랜드 -->
            <template v-else-if="post_type.value === 'BRAND'">
              <div class="card--brand grid-cols-5">
                <v-card v-for="(item, i) in board?.result" :key="i">
                  <NuxtImg
                    :src="(config.CDN_HOST, item.image_url)"
                    class="align-end"
                    height="82"
                    cover
                  />
                  <div class="brand_info">
                    <v-chip
                      size="small"
                      color="sub"
                      variant="flat"
                      class="mr-1"
                      density="comfortable"
                    >
                      {{ enums.brand_ctgry[item.brand_ctgry] }}
                    </v-chip>
                    <p class="text-white">
                      {{ item.brand_kor }}
                    </p>
                  </div>
                </v-card>
              </div>
            </template>
          </div>

          <template v-if="board?.paging">
            <Paging
              v-if="post_type.value === 'NEWS' || post_type.value === 'REPORT'"
              :paging="filter"
              :total_row="total_cnt"
              @changePage="changePage"
            />
          </template>
        </div>
      </template>
    </div>
  </div>
</template>

<style scoped>
.card--brand {
  margin: 1rem auto 2.125rem;
  row-gap: 1.25rem;
}
</style>
