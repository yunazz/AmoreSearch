<script>
definePageMeta({
  layout: false,
});
</script>
<template>
  <div id="loginPage">
    <div class="login_left">
      <div>
        <h2 class="title--xl fw-600">환영합니다!</h2>
        <p class="title--l mt-1 fw-700">AmoreSearch와 함께하는 더 나은 내일</p>
        <p class="my-6">
          <span>우리 회사의 업무를 지원하고,</span>
          <br />
          <span>화장품 산업에서 중요한 혁신을 이끌어가도록 돕겠습니다.</span>
        </p>
        <p class="fw-600">로그인하고 효율적인 업무 시작하세요!</p>
      </div>
    </div>
    <div class="login_right">
      <div class="login_form">
        <v-text-field
          :loading="loading"
          density="compact"
          label="사원번호"
          variant="solo"
          hide-details
          single-line
          @click:append-inner="onClick"
        ></v-text-field>
      </div>
    </div>
  </div>
</template>

<style scoped>
#loginPage {
  display: flex;
  height: 100vh;
}
.login_left,
.login_right {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.login_left {
  width: 50%;
  background: #eef1fc;
}
.login_left > div {
  min-width: 460px;
}
.login_right {
  width: 52%;
  align-items: center;
}
.login_form {
  width: 300px;
}
</style>
