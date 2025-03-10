<script setup>
const member = useMember();
const resultMode = ref(false);
const pending = ref(false);
const filter = ref({
  tag: "",
});
const tags = ref(["검색태그 1", "검색태그 2", "검색태그 3", "검색태그 4"]);

async function search(query) {
  resultMode.value = true;
  pending.value = true;

  setTimeout(() => {
    pending.value = false;
  }, 10000);

  // body = {
  // query: query,
  // tag:};
  // const result = $http("/ai-search", {
  //   key: "ai-search",
  //   body,
  // });
  // pending.value = false;
}
</script>

<template>
  <div id="AiSearch" class="content">
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
                  style="font-size: 15px; font-weight: 500; padding: 20px 22px"
                />
              </v-chip-group>
            </div>
          </div>
        </div>
      </template>
      <template v-else>
        <template v-if="pending">
          <div>결과 출력중</div>
        </template>
        <template v-else>
          <div>출력완료</div>
        </template>
      </template>
    </ClientOnly>
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
