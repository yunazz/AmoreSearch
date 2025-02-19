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
    <div>
      <h2 class="title--xl fw-700">
        안녕하세요,
        <span class="text-underline ml-1">
          {{ member.name }} {{ member.position }}님
        </span>
        <br />무엇을 도와드릴까요?
      </h2>
    </div>
    <div>
      <v-text-field
        append-inner-icon="mdi-magnify"
        density="compact"
        label="Search templates"
        variant="solo"
        hide-details
        single-line
      ></v-text-field>
    </div>
  </div>
</template>

<style scoped>
#AiSearch {
  padding-top: 50px;
}
#AiSearch h2 {
  text-align: center;
  font-size: 2rem;
  line-height: 2.8125rem;
  word-spacing: -4px;
}
.text-underline {
  font-weight: 800;
  text-underline-offset: 7px;
}
</style>
