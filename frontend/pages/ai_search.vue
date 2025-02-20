<script setup>
const member = useMember();
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
        <v-icon icon="mdi-magnify" />
        <input type="text" />
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
  font-size: 1.75rem;
  line-height: 2.5rem;
  word-spacing: -4px;
}
.text-underline {
  font-weight: 800;
  text-underline-offset: 7px;
}
.input--search {
  display: flex;
  align-items: center;
  margin-top: 2px;
}
.input--search input {
  width: 100%;
  outline: none;
}
.input--search i {
  font-size: 34px;
}
</style>
