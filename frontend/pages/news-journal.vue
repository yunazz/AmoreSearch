<script setup>
const tabs = ref([
  { text: "뉴스", value: "NEWS" },
  { text: "저널", value: "JOURNAL" },
]);
const post_type = ref({ text: "회사뉴스", value: "NEWS" });
const source_name = ref({
  name: "코스인코리아닷컴",
  value: "코스인코리아닷컴",
});

const filter = ref({
  post_type: "NEWS",
  source_name: "코스인코리아닷컴",
  current_page: 1,
  item_per_page: 20,
});

const filter_query = computed(() => ({
  post_type: filter.value.post_type,
  source_name: filter.value.source_name,
  current_page: filter.value.current_page,
  item_per_page: filter.value.item_per_page,
}));

function changePage(current_page) {
  if (current_page === filter.value.current_page) {
    return;
  }
  filter.value.current_page = current_page;
  scrollToTop();
}

const { data: board, status } = useApi("/post/external", {
  key: "post-board",
  query: filter_query,
});

watch(post_type, (newValue) => {
  filter.value.post_type = newValue.value;
  source_name.value = externalCategory[newValue.value][0];
  filter.value.source_name = source_name.value.value;
  filter.value.current_page = 1;
});
watch(source_name, (newValue) => {
  filter.value.source_name = newValue.value;
  filter.value.current_page = 1;
});

const total_cnt = computed(() => board.value.paging?.total_rows);
</script>

<template>
  <div id="NewsJournal" class="content">
    <div class="content_inner">
      <div class="page_header">
        <h2 class="page_title">뉴스 / 저널</h2>
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
            <v-btn-toggle v-model="source_name" mandatory rounded="0">
              <v-btn
                v-for="(board, index) in externalCategory[post_type.value]"
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
      <div class="board">
        <div class="board_list">
          <template v-if="status === 'success'">
            <ListItemLink
              v-for="(item, index) in board.result"
              :key="index"
              :item="item"
            />
          </template>
        </div>
        <template v-if="board?.paging">
          <Paging
            :paging="filter"
            :total_row="total_cnt"
            @changePage="changePage"
          />
        </template>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
