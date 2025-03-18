<script setup>
const member = useMember();
const config = useRuntimeConfig().public;

let controller = new AbortController();

const filter = ref({ query: " ", tag: "" });
const tags = ref(["화장품", "성분", "사내문서"]);
const paging = ref({ current_page: 1, item_per_page: 4 });

const resultMode = ref(true);
const active_tab = ref(1);

const requesting = ref(false);
const streaming = ref(false);
const search_input = ref("");
const search_repsonse_parsed = ref({
  llm_response: "",
  db_response: {},
  questions: [
    "관련 질문 내용입니다. 무엇이 궁금할까요?",
    "관련 질문 내용입니다. 무엇이 궁금할까요?",
    "관련 질문 내용입니다. 무엇이 궁금할까요?",
    "관련 질문 내용입니다. 무엇이 궁금할까요?",
  ],
});
const search_repsonse_string = ref("");

const search_response_llm = computed(() => {
  let response_str = search_repsonse_string.value;

  if (!search_repsonse_string.value.includes('{"llm_response": "')) return "";

  response_str = response_str.replace(/^{"llm_response":\s*"/, "");
  response_str = response_str.split('", "db')[0];

  return response_str.replace(/"$/, "");
});

const items = [
  {
    title: "일리윤, 세라마이드 아토 라인 3세대 출시",
    content:
      "Trevor Hansen CDP는 전 세계 금융투자기관이 주도하여 기업에게 환경 관련 경영정보공개를 요청하는 글로벌 이니셔티브다. 매년 기업들이 공개한 정보를 바탕으로 세계 최대 규모의 환경 데이터베이스를 보유하고 있으며, 전 세계 금융기관이 기업 투자와 대출 등의 의사결정에 의미 있는 정보로 활용할 수 있게 지원하여 저탄소 사회와 지속가능한 사회를 위한 기반을 만들어가고 있다. CDP는 기후 및 물 관련 리스크에 대한 대응, 도전적인 감축 목표, 리더십과 관리체계 등을 기반으로 기업을 평가하며 매년 전 세계 23,200개 이상의 기업이 응답하고 있다.",
    post_type: "NEWS",
    created_at: new Date(),
    source_name: "코스메틱리포트",
    source_url: "",
  },
  {
    title: "아모레퍼시픽, CDP 평가에서 2개 부문 모두 최고 등급 획득",
    content: `to Ale Jennifer 아모레퍼시픽은 이번 평가를 포함해 3년 연속 기후변화 대응 부문 A를 획득하며 기후변화에 대한 투명성 분야의 리더십을 인정받았다. 올해 처음으로 획득한 수자원 관리 부문에서도 수자원의 효율적인 사용과 관리, 순환 사용, 수질오염 방지 등에 대한 노력을 인정받아 최고 등급인 A를 받았다.`,
    post_type: "JOURNAL",
    created_at: new Date(),
    source_name: "코스메틱리포트",
    source_url: "",
  },
  {
    title: "설화수, 노스텔지어와 함께 한국 고가구 전시 진행",
    content:
      "Sandra Adams &mdash;아모레퍼시픽은 자사 사업장 내에서 발생하는 온실가스 직접배출량(Scope1)과 전기 등을 구매하면서 발생하는 간접배출량(Scope2)의 총량을 2020년 대비 2050년까지 90% 감축하여 넷제로를 달성하려는 목표를 수립했다. 그 계획의 일환으로 아모레퍼시픽은 적극적인 전사 재생에너지 전환을 추진하고 있으며, 그 결과 2024년 기준 설화수, 라네즈, 해피바스를 비롯한 아모레퍼시픽의 주요 제품을 생산하는 오산, 대전, 안성, 상해 사업장 및 물류 사업장의 재생 전력 100%를 달성했다. 2025년은 아모레퍼시픽 전사 단위의 RE100 달성을 목표로 하고 있다.",
    post_type: "REPORT",
    post_ctgry: "경영성과",
    created_at: new Date(),
    original_file_url: "/",
  },
  {
    title: "일리윤, 세라마이드 아토 라인 3세대 출시",
    content:
      "Trevor Hansen CDP는 전 세계 금융투자기관이 주도하여 기업에게 환경 관련 경영정보공개를 요청하는 글로벌 이니셔티브다. 매년 기업들이 공개한 정보를 바탕으로 세계 최대 규모의 환경 데이터베이스를 보유하고 있으며, 전 세계 금융기관이 기업 투자와 대출 등의 의사결정에 의미 있는 정보로 활용할 수 있게 지원하여 저탄소 사회와 지속가능한 사회를 위한 기반을 만들어가고 있다. CDP는 기후 및 물 관련 리스크에 대한 대응, 도전적인 감축 목표, 리더십과 관리체계 등을 기반으로 기업을 평가하며 매년 전 세계 23,200개 이상의 기업이 응답하고 있다.",
    post_type: "REPORT",
    post_ctgry: "사업보고서",
    created_at: new Date(),
    original_file_url: "/",
  },
  {
    title: "일리윤, 세라마이드 아토 라인 3세대 출시",
    content:
      "Trevor Hansen CDP는 전 세계 금융투자기관이 주도하여 기업에게 환경 관련 경영정보공개를 요청하는 글로벌 이니셔티브다. 매년 기업들이 공개한 정보를 바탕으로 세계 최대 규모의 환경 데이터베이스를 보유하고 있으며, 전 세계 금융기관이 기업 투자와 대출 등의 의사결정에 의미 있는 정보로 활용할 수 있게 지원하여 저탄소 사회와 지속가능한 사회를 위한 기반을 만들어가고 있다. CDP는 기후 및 물 관련 리스크에 대한 대응, 도전적인 감축 목표, 리더십과 관리체계 등을 기반으로 기업을 평가하며 매년 전 세계 23,200개 이상의 기업이 응답하고 있다.",
    post_type: "NEWS",
    created_at: new Date(),
    source_name: "코스메틱리포트",
    source_url: "",
  },
];

const paginatedItems = computed(() => {
  const startIndex =
    (paging.value.current_page - 1) * paging.value.item_per_page;
  const endIndex = startIndex + paging.value.item_per_page;
  return items.slice(startIndex, endIndex);
});

async function search(query) {
  if (query.length === 0) return;
  if (streaming.value || requesting.value) return;

  filter.value.query = query;
  resultMode.value = true;
  requesting.value = true;

  search_input.value = "";
  requesting.value = false;
  // controller = new AbortController();

  // const response = await fetch(
  //   `${config.SERVER_HOST}/api/search/ai?query=${query}`,
  //   {
  //     signal: controller.signal,
  //   }
  // );

  // if (!response.body) {
  //   console.error("스트리밍 응답을 받을 수 없습니다.");
  //   requesting.value = false;
  //   streaming.value = false;
  //   return;
  // }

  // const reader = response.body.getReader();
  // const decoder = new TextDecoder();

  // while (true) {
  //   const { done, value } = await reader.read();
  //   if (done) {
  //     requesting.value = false;
  //     streaming.value = false;
  //     break;
  //   }
  //   if (requesting.value) requesting.value = false;
  //   search_repsonse_string.value += decoder.decode(value, { stream: true });
  // }

  // search_repsonse_parsed.value = JSON.parse(search_repsonse_string.value);
}

function changePage(page) {
  paging.value.current_page = page;
}

function initSearch() {
  resultMode.value = false;
  active_tab.value = 1;
  paging.value.current_page = 1;
  filter.value.query = "";
  search_input.value = "";
  search_repsonse_parsed.value = { llm_response: "", db_response: {} };
  search_repsonse_string.value = "";
}

// watch(
//   () => resultMode,
//   (newValue) => {
//     if (!newValue) {
//       console.log("요청 중단");
//       controller.abort();
//     }
//   }
// );

// onUnmounted(() => {
//   console.log("요청 중단 필요");
//   controller.abort();
// });
</script>

<template>
  <div id="AiSearch" class="content">
    <div class="content_inner">
      <ClientOnly>
        <template v-if="!resultMode">
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
                  style="font-size: 15px; font-weight: 500; padding: 20px 22px"
                />
              </v-chip-group>
            </div>
          </div>
        </template>
        <template v-else>
          <div class="search_result">
            <div class="search_result_cont">
              <div class="search_result_left">
                <!-- 검색 쿼리 -->
                <h3 class="flex align-start col-gap-2 my-5">
                  <v-icon icon="mdi-magnify" color="primary" size="30" />
                  <p>
                    {{ filter.query }}
                    <button v-if="!requesting" @click="initSearch">
                      <v-icon
                        style="margin-bottom: 2px"
                        icon="mdi-close"
                        size="x-small"
                        color="primary"
                      />
                    </button>
                  </p>
                </h3>

                <!-- 검색 결과 -->
                <template v-if="!requesting">
                  <div class="llm_cont" v-html="search_response_llm"></div>

                  <div class="question_cont">
                    <div
                      v-for="(
                        question, index
                      ) in search_repsonse_parsed.questions"
                      :key="index"
                      class="question_item"
                    >
                      <div class="flex">
                        <span>{{ index + 1 }}</span>
                        <p>{{ question }}</p>
                      </div>
                      <div>
                        <v-icon
                          icon="mdi-arrow-right"
                          class="mr-5 text-gray-02"
                        ></v-icon>
                      </div>
                    </div>
                  </div>
                  <div class="cosmetic_cont"></div>
                </template>

                <!-- 검색중 -->
                <template v-else>
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
              </div>

              <div v-if="!requesting" class="search_result_right">
                <p class="mt-5 fw-600">
                  <button
                    class="btn--text"
                    :class="{ active: active_tab == 1 }"
                    @click="active_tab = 1"
                  >
                    검색 문서
                  </button>
                  <button
                    class="btn--text"
                    :class="{ active: active_tab == 2 }"
                    @click="active_tab = 2"
                  >
                    출처 자료
                  </button>
                </p>
                <!-- tab 1  -->
                <template v-if="active_tab === 1">
                  <ListItemReference
                    v-for="(item, index) in paginatedItems"
                    :key="index"
                    :item="item"
                  />
                  <Paging
                    :paging="paging"
                    :total_row="items.length"
                    :first-page="false"
                    :last-page="false"
                    @changePage="changePage"
                  />
                </template>

                <!-- 우측 tab 1  -->
                <template v-else-if="active_tab === 2"> 출처 리스트 </template>
              </div>
            </div>

            <!-- input gradient bg-->
            <div class="block_bg_box" />
            <!-- 하단 검색 Input -->
            <div class="search_input_cont">
              <label for="search_input">
                <v-icon icon="mdi-magnify" color="primary" />
              </label>
              <input
                id="search_input"
                type="text"
                v-model="search_input"
                @keydown.enter="search(search_input)"
                placeholder=""
                :disabled="requesting"
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
.content_inner {
  position: relative;
  padding-right: 12px;
  padding-left: 28px;
  margin-bottom: 28px;
}
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
#AiSearch .paging {
  margin-top: 1rem;
  margin-bottom: 0.25rem;
}
#AiSearch.content {
  max-width: 100%;
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
  line-height: 1.2;
}
.search_result .search_result_left {
  flex: 1;
  margin-bottom: 3rem;
  margin-right: 1.5rem;
}
.search_result .search_result_right {
  width: 340px;
  margin-bottom: 3rem;
  display: flex;
  flex-direction: column;
  row-gap: 12px;
}
.search_input_cont {
  position: fixed;
  z-index: 2;
  bottom: 16px;
  left: 216px;
  width: calc(100% - 230px);
  box-shadow: rgba(0, 0, 0, 0.12) 0px 1px 3px, rgba(0, 0, 0, 0.24) 0px 1px 2px;
}

.block_bg_box {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 84px;
  background: linear-gradient(
    180deg,
    rgba(255, 255, 255, 0) 0%,
    rgba(255, 255, 255, 1) 35%
  );
  z-index: 1;
}

button.btn--text {
  font-size: 1.125rem;
  margin-right: 1.75rem;
  transition: all 0.2s ease;
  word-spacing: -1px;
  color: var(--color-gray-03);
}
button.btn--text:hover {
  color: var(--sub-color);
}
button.btn--text.active {
  color: var(--color-black);
}
.llm_cont {
  min-height: 300px;
}

.question_cont {
  margin-top: 2rem;
}
.question_item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 45px;
  border-bottom: 1px solid var(--border-color);
  font-size: 14px;
  cursor: pointer;
  user-select: none;
  background: #fff;
  transition: all 0.1s ease;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
.question_item:hover {
  background: var(--sub-light-color);
}
.question_item:nth-child(1) {
  border-top: 1px solid var(--border-color);
}
.question_item > div {
  display: flex;
  align-items: center;
}
.question_item span {
  margin-left: 8px;
  margin-right: 2px;
  font-weight: 700;
  color: var(--main-color);
  padding: 0 12px;
  font-size: 15px;
}
.question_item p {
  font-size: 13px;
}
.question_item i {
  transition: all 0.15s ease;
}
.question_item:hover i {
  margin-right: 16px !important;
}
</style>
