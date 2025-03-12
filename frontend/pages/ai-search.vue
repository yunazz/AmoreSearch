<script setup>
const member = useMember();
const resultMode = ref(false);
const pending = ref(false);
const filter = ref({
  query: "미백 기능을 가진 화장품을 소개해줘",
  tag: "",
});
const tags = ref(["검색태그 1", "검색태그 2", "검색태그 3", "검색태그 4"]);

async function search(query) {
  if (query.length === 0) return;
  filter.value.query = query;
  resultMode.value = true;
  pending.value = true;

  setTimeout(() => {
    pending.value = false;
  }, 3000);

  // body = {
  // query: query,
  // tag:};
  // const result = $http("/ai-search", {
  //   key: "ai-search",
  //   body,
  // });
  // pending.value = false;
}
function initSearch() {
  resultMode.value = false;
  filter.value.query = "";
}
</script>

<template>
  <div id="AiSearch" class="content">
    <div class="content_inner">
      <ClientOnly>
        <template v-if="!resultMode">
          <div class="content_inner">
            <div class="content_center">
              <h2 class="fw-700 gradient-text mb-6">
                안녕하세요,
                <span class="ml-1">
                  {{ member.name }} {{ member.position }}님
                </span>
                <br />
                무엇을 도와드릴까요?
              </h2>

              <div>
                <SearchInput
                  :texts="[
                    '최근에 출시한 우리회사 제품들을 소개해줘',
                    '선크림에 주요한 성분들에 대해서 알려줘',
                  ]"
                  @search="search"
                />
              </div>
              <div class="flex justify-center mt-6">
                <v-chip-group
                  v-model="filter.tag"
                  selected-class="text-primary"
                  mandatory
                >
                  <v-chip
                    filter
                    v-for="tag in tags"
                    :key="tag"
                    :text="tag"
                    :value="tag"
                    style="
                      font-size: 15px;
                      font-weight: 500;
                      padding: 20px 22px;
                    "
                  />
                </v-chip-group>
              </div>
            </div>
          </div>
        </template>
        <template v-else>
          <div class="search_result">
            <h3 class="flex align-center col-gap-2 my-5">
              <v-icon icon="mdi-magnify" color="primary" />
              {{ filter.query }}
              <button v-if="!pending" class="flex" @click="initSearch">
                <v-icon icon="mdi-close" size="x-small" color="primary" />
              </button>
            </h3>

            <div class="search_result_cont">
              <div class="search_result_left">
                <template v-if="pending">
                  <div>
                    <v-progress-linear
                      style="width: 60%"
                      class="progress_linear_primary mb-3"
                      indeterminate
                      rounded
                      height="15"
                    />
                    <v-progress-linear
                      style="width: 50%"
                      class="progress_linear_primary mb-3"
                      indeterminate
                      rounded
                      height="15"
                    />
                    <v-progress-linear
                      style="width: 40%"
                      class="progress_linear_primary mb-3"
                      indeterminate
                      rounded
                      height="15"
                    />
                  </div>
                </template>
                <template v-else>
                  <div>출력결과</div>
                </template>
              </div>
              <div class="search_result_right">기사</div>
            </div>

            <div class="search_input_cont">
              <label for="search_input">
                <v-icon icon="mdi-magnify" color="primary" />
              </label>
              <input
                id="search_input"
                type="text"
                v-model="search_input"
                @keydown.enter="search"
                placeholder=""
                :disabled="pending"
                style="outline: none"
              />
            </div>
          </div>
        </template>
      </ClientOnly>
    </div>
  </div>
</template>

<style scoped>
#AiSearch h2 {
  display: inline-block;
  font-size: 38px;
  text-align: center;
  line-height: 48px;
  word-spacing: -4px;
  font-weight: 800;
  margin: 0 auto;
  animation: fadeInDown2 0.8s;
}
#AiSearch .grid-cols-2 {
  column-gap: 2rem;
}
.content_center {
  width: 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 0 80px 130px;
}

.group_card {
  margin: 0 auto;
  width: calc(100vw - 280px);
  min-width: 1040px;
  max-width: 1400px;
}
.group_card_item {
  height: 200px;
  min-width: 295px;
  width: calc((100vw - 360px) / 5);
  border-radius: var(--radius-3);
  /* border: 1px solid var(--border-color); */
  background: #e5e5e5;
  margin-right: 16px;
}
.group_card_item:last-of-type {
  margin-right: 0;
}
.group_card_item .card_img {
  border-radius: var(--radius-3);
}

.search_result {
  display: flex;
  flex-direction: column;
}
.search_result > .search_result_cont {
  display: flex;
  min-height: calc(100vh - 100px);
}
.search_result h3 {
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
}
.search_result .search_result_left {
  margin-bottom: 3rem;
  flex: 1;
}
.search_result .search_result_right {
  width: 300px;
  margin-bottom: 3rem;

  border-left: 1px solid var(--border-color);
}
.search_input_cont {
  position: fixed;
  bottom: 10px;
  left: 210px;
  width: calc(100% - 220px);
}
</style>
