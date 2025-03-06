<script setup>
const member = useMember();
const tag = ref("검색태그 1");
const tags = ref(["검색태그 1", "검색태그 2", "검색태그 3", "검색태그 4"]);
const items = [
  { type: "subheader", title: "아모레 뉴스" },
  {
    title: "아모레퍼시픽, CDP 평가에서 2개 부문 모두 최고 등급 획득",
    subtitle: `<span class="text-primary">to Alex, Scott, Jennifer</span>아모레퍼시픽은 이번 평가를 포함해 3년 연속 기후변화 대응 부문 A를 획득하며 기후변화에 대한 투명성 분야의 리더십을 인정받았다. 올해 처음으로 획득한 수자원 관리 부문에서도 수자원의 효율적인 사용과 관리, 순환 사용, 수질오염 방지 등에 대한 노력을 인정받아 최고 등급인 A를 받았다.`,
  },
  {
    title: "일리윤, 세라마이드 아토 라인 3세대 출시",
    subtitle:
      '<span class="text-primary">Trevor Hansen</span> CDP는 전 세계 금융투자기관이 주도하여 기업에게 환경 관련 경영정보공개를 요청하는 글로벌 이니셔티브다. 매년 기업들이 공개한 정보를 바탕으로 세계 최대 규모의 환경 데이터베이스를 보유하고 있으며, 전 세계 금융기관이 기업 투자와 대출 등의 의사결정에 의미 있는 정보로 활용할 수 있게 지원하여 저탄소 사회와 지속가능한 사회를 위한 기반을 만들어가고 있다. CDP는 기후 및 물 관련 리스크에 대한 대응, 도전적인 감축 목표, 리더십과 관리체계 등을 기반으로 기업을 평가하며 매년 전 세계 23,200개 이상의 기업이 응답하고 있다.',
  },
  {
    title: "설화수, 노스텔지어와 함께 한국 고가구 전시 진행",
    subtitle:
      '<span class="text-primary">Sandra Adams</span> &mdash;아모레퍼시픽은 자사 사업장 내에서 발생하는 온실가스 직접배출량(Scope1)과 전기 등을 구매하면서 발생하는 간접배출량(Scope2)의 총량을 2020년 대비 2050년까지 90% 감축하여 넷제로를 달성하려는 목표를 수립했다. 그 계획의 일환으로 아모레퍼시픽은 적극적인 전사 재생에너지 전환을 추진하고 있으며, 그 결과 2024년 기준 설화수, 라네즈, 해피바스를 비롯한 아모레퍼시픽의 주요 제품을 생산하는 오산, 대전, 안성, 상해 사업장 및 물류 사업장의 재생 전력 100%를 달성했다. 2025년은 아모레퍼시픽 전사 단위의 RE100 달성을 목표로 하고 있다.',
  },

  {
    title: "일리윤, 세라마이드 아토 라인 3세대 출시",
    subtitle:
      '<span class="text-primary">Trevor Hansen</span> CDP는 전 세계 금융투자기관이 주도하여 기업에게 환경 관련 경영정보공개를 요청하는 글로벌 이니셔티브다. 매년 기업들이 공개한 정보를 바탕으로 세계 최대 규모의 환경 데이터베이스를 보유하고 있으며, 전 세계 금융기관이 기업 투자와 대출 등의 의사결정에 의미 있는 정보로 활용할 수 있게 지원하여 저탄소 사회와 지속가능한 사회를 위한 기반을 만들어가고 있다. CDP는 기후 및 물 관련 리스크에 대한 대응, 도전적인 감축 목표, 리더십과 관리체계 등을 기반으로 기업을 평가하며 매년 전 세계 23,200개 이상의 기업이 응답하고 있다.',
  },
];
const items1 = [
  { type: "subheader", title: "외부자료/저널" },
  {
    title: "일리윤, 세라마이드 아토 라인 3세대 출시",
    subtitle:
      '<span class="text-primary">Trevor Hansen</span> CDP는 전 세계 금융투자기관이 주도하여 기업에게 환경 관련 경영정보공개를 요청하는 글로벌 이니셔티브다. 매년 기업들이 공개한 정보를 바탕으로 세계 최대 규모의 환경 데이터베이스를 보유하고 있으며, 전 세계 금융기관이 기업 투자와 대출 등의 의사결정에 의미 있는 정보로 활용할 수 있게 지원하여 저탄소 사회와 지속가능한 사회를 위한 기반을 만들어가고 있다. CDP는 기후 및 물 관련 리스크에 대한 대응, 도전적인 감축 목표, 리더십과 관리체계 등을 기반으로 기업을 평가하며 매년 전 세계 23,200개 이상의 기업이 응답하고 있다.',
  },
  {
    title: "아모레퍼시픽, CDP 평가에서 2개 부문 모두 최고 등급 획득",
    subtitle: `<span class="text-primary">to Alex, Scott, Jennifer</span>아모레퍼시픽은 이번 평가를 포함해 3년 연속 기후변화 대응 부문 A를 획득하며 기후변화에 대한 투명성 분야의 리더십을 인정받았다. 올해 처음으로 획득한 수자원 관리 부문에서도 수자원의 효율적인 사용과 관리, 순환 사용, 수질오염 방지 등에 대한 노력을 인정받아 최고 등급인 A를 받았다.`,
  },
  {
    title: "설화수, 노스텔지어와 함께 한국 고가구 전시 진행",
    subtitle:
      '<span class="text-primary">Sandra Adams</span> &mdash;아모레퍼시픽은 자사 사업장 내에서 발생하는 온실가스 직접배출량(Scope1)과 전기 등을 구매하면서 발생하는 간접배출량(Scope2)의 총량을 2020년 대비 2050년까지 90% 감축하여 넷제로를 달성하려는 목표를 수립했다. 그 계획의 일환으로 아모레퍼시픽은 적극적인 전사 재생에너지 전환을 추진하고 있으며, 그 결과 2024년 기준 설화수, 라네즈, 해피바스를 비롯한 아모레퍼시픽의 주요 제품을 생산하는 오산, 대전, 안성, 상해 사업장 및 물류 사업장의 재생 전력 100%를 달성했다. 2025년은 아모레퍼시픽 전사 단위의 RE100 달성을 목표로 하고 있다.',
  },
  {
    title: "일리윤, 세라마이드 아토 라인 3세대 출시",
    subtitle:
      '<span class="text-primary">Trevor Hansen</span> CDP는 전 세계 금융투자기관이 주도하여 기업에게 환경 관련 경영정보공개를 요청하는 글로벌 이니셔티브다. 매년 기업들이 공개한 정보를 바탕으로 세계 최대 규모의 환경 데이터베이스를 보유하고 있으며, 전 세계 금융기관이 기업 투자와 대출 등의 의사결정에 의미 있는 정보로 활용할 수 있게 지원하여 저탄소 사회와 지속가능한 사회를 위한 기반을 만들어가고 있다. CDP는 기후 및 물 관련 리스크에 대한 대응, 도전적인 감축 목표, 리더십과 관리체계 등을 기반으로 기업을 평가하며 매년 전 세계 23,200개 이상의 기업이 응답하고 있다.',
  },
];
</script>

<template>
  <div id="AiSearch" class="content">
    <div class="content_inner">
      <ClientOnly>
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
            />
          </div>
          <div class="flex justify-center mt-6">
            <v-chip-group v-model="tag" selected-class="text-primary" mandatory>
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
  min-width: 1000px;
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
</style>
