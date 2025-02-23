<script setup>
const props = defineProps({
  paging: { type: Object, required: true },
  totalRows: { required: true, default: 0 },
  disabled: { type: Boolean, default: false },
  board_type: { type: String, default: "" },
});
const emit = defineEmits(["changePage"]);
const pagePerGroup = 10;

const paging = ref({
  currentPage: props.paging.currentPage,
  pagePerGroup: props.paging.pagePerGroup,
  totalRows: Number(props.totalRows),
  lastPage: 1,
  groupStartPage: 1,
  groupEndPage: 1,
  pageList: [1],
});
set_paging_data();
watch(
  () => props.paging.currentPage,
  (newValue) => {
    paging.value.currentPage = newValue;
    set_paging_data();
  }
);

watch(
  () => props.paging.pagePerGroup,
  (newValue) => {
    paging.value.pagePerGroup = newValue;
    set_paging_data();
  }
);

function groupEndPage() {
  const groupEndPageVal =
    Math.ceil(paging.value.currentPage / pagePerGroup) * pagePerGroup;
  return groupEndPageVal < paging.value.lastPage
    ? groupEndPageVal
    : paging.value.lastPage;
}

function groupStartPage() {
  return (
    Math.floor((paging.value.currentPage - 1) / pagePerGroup) * pagePerGroup + 1
  );
}

function set_paging_data() {
  paging.value.pageList = [];
  paging.value.lastPage =
    paging.value.totalRows == 0
      ? 1
      : Math.ceil(Number(paging.value.totalRows) / paging.value.pagePerGroup);
  paging.value.groupStartPage = groupStartPage();
  paging.value.groupEndPage = groupEndPage();

  if (paging.value.groupEndPage > 0) {
    for (
      let i = paging.value.groupStartPage;
      i <= paging.value.groupEndPage;
      i++
    ) {
      paging.value.pageList.push(i);
    }
  }
}

const changePage = (page, board_type) => {
  if (props.disabled) {
    return;
  }
  let _page = page;
  if (page <= 0) _page = 1;
  if (page >= paging.value.lastPage) _page = paging.value.lastPage;

  emit("changePage", _page, props.board_type);
};
</script>
<template>
  <div class="paging">
    <!-- <button
      @click="changePage(1)"
      :class="{
        hide: paging.currentPage === 1 || paging.currentPage <= pagePerGroup,
      }"
    >
      <v-icon icon="mdi-page-first" />
    </button> -->
    <button
      @click="changePage(paging.groupStartPage - pagePerGroup)"
      :class="{
        hide: paging.currentPage === 1 || paging.groupStartPage < pagePerGroup,
      }"
    >
      <v-icon icon="mdi-chevron-left" />
    </button>
    <div class="paging_num">
      <button
        v-for="item in paging.pageList"
        :key="item"
        :class="{ active: paging.currentPage === item }"
        @click="changePage(item)"
      >
        {{ item }}
      </button>
    </div>
    <button
      :class="{
        hide:
          paging.currentPage === paging.lastPage ||
          paging.groupStartPage + 9 >= paging.lastPage,
      }"
      @click="changePage(paging.groupEndPage + 1)"
    >
      <v-icon icon="mdi-chevron-right" />
    </button>
    <!-- <button
      :class="{
        hide:
          paging.lastPage === paging.currentPage ||
          paging.groupEndPage - paging.groupStartPage < pagePerGroup,
      }"
      @click="changePage(paging.lastPage)"
    >
      <v-icon icon="mdi-page-last" />
    </button> -->
  </div>
</template>
<style scoped>
.paging {
  display: flex;
  justify-content: center;
  align-items: center;
  column-gap: 0.5rem;
  margin-bottom: 2rem;
}
.paging_num {
  display: flex;
  align-items: center;
  column-gap: 0.5rem;
}
.paging_num button {
  padding: 4px;
}
.paging_num button.active {
  font-weight: 600;
  color: var(--main-color);
  padding: 4px;
}
.paging .hide {
  opacity: 0;
  pointer-events: none;
}
</style>
