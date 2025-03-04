<script setup>
const config = useRuntimeConfig().public;
const show = ref(true);
const tab = ref("BRAND");
const tabs = [
  { text: "회사뉴스", value: "NEWS" },
  { text: "브랜드", value: "BRAND" },
  { text: "IR자료", value: "IR" },
  { text: "사내문서", value: "DOCUMENT" },
];
const filter_tag = ref({ name: "전체", value: "" });

const filter = ref({
  currentPage: 1,
  pagePerGroup: 20,
});

const brand_query = computed(() => ({
  brand_ctgry: filter_tag.value.value,
  current_page: filter.value.currentPage,
  page_per_group: 20,
}));

function changePage(currentPage) {
  if (currentPage === filter.value.currentPage) {
    return;
  }
  filter.value.currentPage = currentPage;
  scrollToTop();
}
function changeBoard(board) {
  filter_tag.value = board;
}
const list1 = ref([
  {
    title: "회사뉴스 제목",
    subtitle: "subtitle을 넣을 수 있음",
    img_url: "https://cdn.vuetifyjs.com/images/cards/sunshine.jpg",
    registered_at: "2025-01-01",
  },
  {
    title: "회사뉴스 제목",
    subtitle: "subtitle을 넣을 수 있음",
    img_url: "https://cdn.vuetifyjs.com/images/cards/sunshine.jpg",
    registered_at: "2025-01-01",
  },
  {
    title: "회사뉴스 제목",
    subtitle: "subtitle을 넣을 수 있음",
    img_url: "https://cdn.vuetifyjs.com/images/cards/sunshine.jpg",
    registered_at: "2025-01-01",
  },
  {
    title: "회사뉴스 제목",
    subtitle: "subtitle을 넣을 수 있음",
    img_url: "https://cdn.vuetifyjs.com/images/cards/sunshine.jpg",
    registered_at: "2025-01-01",
  },
  {
    title: "회사뉴스 제목",
    subtitle: "subtitle을 넣을 수 있음",
    img_url: "https://cdn.vuetifyjs.com/images/cards/sunshine.jpg",
    registered_at: "2025-01-01",
  },
  {
    title: "회사뉴스 제목",
    subtitle: "subtitle을 넣을 수 있음",
    img_url: "https://cdn.vuetifyjs.com/images/cards/sunshine.jpg",
    registered_at: "2025-01-01",
  },
  {
    title: "회사뉴스 제목",
    subtitle: "subtitle을 넣을 수 있음",
    img_url: "https://cdn.vuetifyjs.com/images/cards/sunshine.jpg",
    registered_at: "2025-01-01",
  },
  {
    title: "회사뉴스 제목",
    subtitle: "subtitle을 넣을 수 있음",
    img_url: "https://cdn.vuetifyjs.com/images/cards/sunshine.jpg",
    registered_at: "2025-01-01",
  },
]);
const { data: brands } = useApi("/amorepacific/brands", {
  key: "amorestory-board",
  query: brand_query.value,
});
const list3 = ref([
  {
    title: "아모레퍼시픽 2024년 1/4분기 경영실적",
    subtitle:
      "CDP는 전 세계 금융투자기관이 주도하여 기업에게 환경 관련 경영정보공개를 요청하는 글로벌 이니셔티브다. 매년 기업들이 공개한 정보를 바탕으로 세계 최대 규모의 환경 데이터베이스를 보유하고 있으며, 전 세계 금융기관이 기업 투자와 대출 등의 의사결정에 의미 있는 정보로 활용할 수 있게 지원하여 저탄소 사회와 지속가능한 사회를 위한 기반을 만들어가고 있다. CDP는 기후 및 물 관련 리스크에 대한 대응, 도전적인 감축 목표, 리더십과 관리체계 등을 기반으로 기업을 평가하며 매년 전 세계 23,200개 이상의 기업이 응답하고 있다.",
  },
  {
    title: "아모레퍼시픽 2024년 기업가치 제고 계획",
    subtitle: `아모레퍼시픽은 이번 평가를 포함해 3년 연속 기후변화 대응 부문 A를 획득하며 기후변화에 대한 투명성 분야의 리더십을 인정받았다. 올해 처음으로 획득한 수자원 관리 부문에서도 수자원의 효율적인 사용과 관리, 순환 사용, 수질오염 방지 등에 대한 노력을 인정받아 최고 등급인 A를 받았다.`,
  },

  {
    title: "아모레퍼시픽 2023년 사업 보고서",
    subtitle:
      "아모레퍼시픽은 자사 사업장 내에서 발생하는 온실가스 직접배출량(Scope1)과 전기 등을 구매하면서 발생하는 간접배출량(Scope2)의 총량을 2020년 대비 2050년까지 90% 감축하여 넷제로를 달성하려는 목표를 수립했다. 그 계획의 일환으로 아모레퍼시픽은 적극적인 전사 재생에너지 전환을 추진하고 있으며, 그 결과 2024년 기준 설화수, 라네즈, 해피바스를 비롯한 아모레퍼시픽의 주요 제품을 생산하는 오산, 대전, 안성, 상해 사업장 및 물류 사업장의 재생 전력 100%를 달성했다. 2025년은 아모레퍼시픽 전사 단위의 RE100 달성을 목표로 하고 있다.",
  },
  {
    title: "아모레퍼시픽 제18기 (2023) 영업보고서",
    subtitle:
      "CDP는 전 세계 금융투자기관이 주도하여 기업에게 환경 관련 경영정보공개를 요청하는 글로벌 이니셔티브다. 매년 기업들이 공개한 정보를 바탕으로 세계 최대 규모의 환경 데이터베이스를 보유하고 있으며, 전 세계 금융기관이 기업 투자와 대출 등의 의사결정에 의미 있는 정보로 활용할 수 있게 지원하여 저탄소 사회와 지속가능한 사회를 위한 기반을 만들어가고 있다. CDP는 기후 및 물 관련 리스크에 대한 대응, 도전적인 감축 목표, 리더십과 관리체계 등을 기반으로 기업을 평가하며 매년 전 세계 23,200개 이상의 기업이 응답하고 있다.",
  },
  {
    title: "아모레퍼시픽 2024년 1/4분기 경영실적",
    subtitle:
      "CDP는 전 세계 금융투자기관이 주도하여 기업에게 환경 관련 경영정보공개를 요청하는 글로벌 이니셔티브다. 매년 기업들이 공개한 정보를 바탕으로 세계 최대 규모의 환경 데이터베이스를 보유하고 있으며, 전 세계 금융기관이 기업 투자와 대출 등의 의사결정에 의미 있는 정보로 활용할 수 있게 지원하여 저탄소 사회와 지속가능한 사회를 위한 기반을 만들어가고 있다. CDP는 기후 및 물 관련 리스크에 대한 대응, 도전적인 감축 목표, 리더십과 관리체계 등을 기반으로 기업을 평가하며 매년 전 세계 23,200개 이상의 기업이 응답하고 있다.",
  },
  {
    title: "아모레퍼시픽 2024년 기업가치 제고 계획",
    subtitle: `아모레퍼시픽은 이번 평가를 포함해 3년 연속 기후변화 대응 부문 A를 획득하며 기후변화에 대한 투명성 분야의 리더십을 인정받았다. 올해 처음으로 획득한 수자원 관리 부문에서도 수자원의 효율적인 사용과 관리, 순환 사용, 수질오염 방지 등에 대한 노력을 인정받아 최고 등급인 A를 받았다.`,
  },
  {
    title: "아모레퍼시픽 2023년 사업 보고서",
    subtitle:
      "아모레퍼시픽은 자사 사업장 내에서 발생하는 온실가스 직접배출량(Scope1)과 전기 등을 구매하면서 발생하는 간접배출량(Scope2)의 총량을 2020년 대비 2050년까지 90% 감축하여 넷제로를 달성하려는 목표를 수립했다. 그 계획의 일환으로 아모레퍼시픽은 적극적인 전사 재생에너지 전환을 추진하고 있으며, 그 결과 2024년 기준 설화수, 라네즈, 해피바스를 비롯한 아모레퍼시픽의 주요 제품을 생산하는 오산, 대전, 안성, 상해 사업장 및 물류 사업장의 재생 전력 100%를 달성했다. 2025년은 아모레퍼시픽 전사 단위의 RE100 달성을 목표로 하고 있다.",
  },
  {
    title: "아모레퍼시픽 제18기 (2023) 영업보고서",
    subtitle:
      "CDP는 전 세계 금융투자기관이 주도하여 기업에게 환경 관련 경영정보공개를 요청하는 글로벌 이니셔티브다. 매년 기업들이 공개한 정보를 바탕으로 세계 최대 규모의 환경 데이터베이스를 보유하고 있으며, 전 세계 금융기관이 기업 투자와 대출 등의 의사결정에 의미 있는 정보로 활용할 수 있게 지원하여 저탄소 사회와 지속가능한 사회를 위한 기반을 만들어가고 있다. CDP는 기후 및 물 관련 리스크에 대한 대응, 도전적인 감축 목표, 리더십과 관리체계 등을 기반으로 기업을 평가하며 매년 전 세계 23,200개 이상의 기업이 응답하고 있다.",
  },
  {
    title: "아모레퍼시픽 2024년 1/4분기 경영실적",
    subtitle:
      "CDP는 전 세계 금융투자기관이 주도하여 기업에게 환경 관련 경영정보공개를 요청하는 글로벌 이니셔티브다. 매년 기업들이 공개한 정보를 바탕으로 세계 최대 규모의 환경 데이터베이스를 보유하고 있으며, 전 세계 금융기관이 기업 투자와 대출 등의 의사결정에 의미 있는 정보로 활용할 수 있게 지원하여 저탄소 사회와 지속가능한 사회를 위한 기반을 만들어가고 있다. CDP는 기후 및 물 관련 리스크에 대한 대응, 도전적인 감축 목표, 리더십과 관리체계 등을 기반으로 기업을 평가하며 매년 전 세계 23,200개 이상의 기업이 응답하고 있다.",
  },
  {
    title: "아모레퍼시픽 2024년 기업가치 제고 계획",
    subtitle: `아모레퍼시픽은 이번 평가를 포함해 3년 연속 기후변화 대응 부문 A를 획득하며 기후변화에 대한 투명성 분야의 리더십을 인정받았다. 올해 처음으로 획득한 수자원 관리 부문에서도 수자원의 효율적인 사용과 관리, 순환 사용, 수질오염 방지 등에 대한 노력을 인정받아 최고 등급인 A를 받았다.`,
  },
]);

function initBoardType() {
  filter_tag.value = "전체";
}
</script>

<template>
  <div id="AmoreStory" class="content">
    <div class="content_inner">
      <div class="page_header">
        <h2 class="page_title">아모레스토리</h2>
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
                @click="initBoardType"
                :ripple="false"
              />
            </v-tabs>
          </ClientOnly>
        </div>
        <div class="board_tab depth-2">
          <ClientOnly>
            <v-btn-toggle v-model="filter_tag" mandatory rounded="0">
              <v-btn
                v-for="(board, index) in boardCategory[tab]"
                :key="index"
                :value="board.value"
                :ripple="false"
                height="40"
                min-width="72"
                selected-class="text-primary"
                @click="changeBoard(board)"
              >
                {{ board.name }}
              </v-btn>
            </v-btn-toggle>
          </ClientOnly>
        </div>
      </div>
      <div class="board">
        <div v-if="tab === 'NEWS' || tab === 'BRAND'" class="board_content">
          <!-- 1 회사뉴스 -->
          <BoardItemCardNews v-if="tab === 'NEWS'" :list="list1" />
          <!-- 2 브랜드 -->
          <div v-if="tab === 'BRAND'" class="card--brand grid-cols-5">
            <v-card v-for="(item, i) in brands.result" :key="i">
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
        </div>
        <div class="board_list" v-else>
          <!-- 3 IR -->
          <BoardItemDocument v-if="tab === 'IR'" :list="list3" />
        </div>

        <Paging
          v-if="tab === 'NEWS' || tab === 'IR'"
          :paging="filter"
          totalRows="10"
          @changePage="changePage"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
.card--brand {
  margin: 1rem auto 2.125rem;
  row-gap: 1.25rem;
}
</style>
