<script setup>
// const router = useRouter();
const member = ref({
  name: "홍길동",
  position: "사원",
  department: "HR",
});
const formData = ref({});
</script>
<template>
  <div id="AiSearch" class="page">
    <div class="contents">
      <h2 class="title--xl fw-700">
        안녕하세요,
        <span class="text-underline ml-1">
          {{ member.name }} {{ member.position }}님
        </span>
        <br />
        무엇을 도와드릴까요?
      </h2>
      <div class="input--search mt-3">
        <v-text-field
          prepend-inner-icon="mdi-magnify"
          variant
          hide-details
          single-line
          density="compact"
        />
      </div>
      <div>
        <div class="card_outlined"></div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.v-field.v-field--prepended {
  border-radius: 34px;
}

#AiSearch h2 {
  /* text-align: center; */
  font-size: 1.75rem;
  line-height: 2.5rem;
  word-spacing: -4px;
}
.text-underline {
  font-weight: 800;
  text-underline-offset: 7px;
}
.input--search {
  margin-top: 2px;
  /* max-width: 800px; */
  /* margin: 0 auto; */
  /* margin-top: 0.75rem; */
}
</style>
