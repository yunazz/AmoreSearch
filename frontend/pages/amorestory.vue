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
  currentPage: 1,
  pagePerGroup: 8,
});

const filter_query = computed(() => ({
  post_type: post_type.value.value,
  post_ctgry: post_ctgry.value.value,
  page_no: filter.value.currentPage,
  page_per_group: filter.value.pagePerGroup,
}));

function changePage(currentPage) {
  if (currentPage === filter.value.currentPage) {
    return;
  }
  filter.value.currentPage = currentPage;
  scrollToTop();
}

function onTabChange(tab) {}

function onCategoryChange(ctgry) {}

const { data: board, status } = useApi("/amorestory/board", {
  key: "amorestory-board",
  query: filter_query,
});

const total_cnt = computed(() => board.value.paging?.total_rows);
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
                @click="onTabChange(tab)"
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
                @click="onCategoryChange(board)"
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
              <BoardItemDocument
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

          <Paging
            v-if="post_type.value === 'NEWS' || post_type.value === 'REPORT'"
            :paging="filter"
            :totalRows="total_cnt"
            @changePage="changePage"
          />
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
