<script setup>
const tabs = ref([
  { text: "뉴스", value: "NEWS" },
  { text: "저널", value: "JOURNAL" },
]);
const tab = ref("NEWS");
const post_type = ref({ text: "회사뉴스", value: "NEWS" });
const post_ctgry = ref({ name: "전체", value: "" });

const filter = ref({
  current_page: 1,
  pagePerGroup: 20,
});

const filter_query = computed(() => ({
  post_type: post_type.value.value,
  source: post_ctgry.value.value,
  current_page: filter.value.current_page,
  page_per_group: filter.value.pagePerGroup,
}));

function changePage(current_page) {
  if (current_page === filter.value.current_page) {
    return;
  }
  filter.value.current_page = current_page;
  scrollToTop();
}

function onTabChange(tab) {}

function onCategoryChange(ctgry) {}

const { data: board, status } = useApi("/amorestory/board", {
  key: "amorestory-board",
  query: filter_query,
});

const totalCnt = computed(() => board.value.paging?.total_rows);
</script>

<template>
  <div id="NewsJournal" class="content">
    <div class="content_inner">
      <div class="page_header">
        <h2 class="page_title">뉴스 / 저널</h2>
        <div class="board_tab depth-1">
          <ClientOnly>
            <v-tabs
              v-model="tab"
              bg-color="transparent"
              align-tabs="center"
              density="comfortable"
              selected-class="text-primary"
            >
              <v-tab
                v-for="tab in tabs"
                :key="tab.value"
                :text="tab.text"
                :value="tab.value"
                :ripple="false"
              />
            </v-tabs>
          </ClientOnly>
        </div>
      </div>
      <div class="board">
        <div class="board_list">
          <template v-if="tab === 'NEWS'">
            <BoardItemLinks :list="board.result" />
          </template>
          <template v-if="tab === 'JOURNAL'">
            <BoardItemLinks :list="board.result" />
          </template>
        </div>

        <Paging
          :paging="filter"
          :totalRows="totalCnt"
          @changePage="changePage"
        />
      </div>
    </div>
  </div>
</template>

<style scoped></style>
