<script setup>
definePageMeta({
  layout: false,
});

const router = useRouter();
const formData = ref({
  identify: "",
  password: "",
});
async function login() {
  // 유효성 체크
  // post
  const response = { code: 0, result: true, msg: "" };
  const { result } = response;
  result ? loginSuccess() : loginFail();
}

function loginSuccess() {
  // 토큰 관련
  router.push("/home");
}

function loginFail(msg) {
  // toast msg
}
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
        <h3 class="text-center fw-600 mb-4">로그인</h3>
        <div class="input_wrap">
          <v-text-field
            :loading="loading"
            density="compact"
            label="사원번호"
            variant="outlined"
            hide-details
            single-line
            @click:append-inner="onClick"
            v-model="formData.emp_no"
          />
          <v-text-field
            :loading="loading"
            density="compact"
            label="비밀번호"
            variant="outlined"
            hide-details
            single-line
            @click:append-inner="onClick"
            v-model="formData.password"
          />
          <v-btn class="w-full" color="primary" @click="login"> 로그인 </v-btn>
        </div>
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
  width: 280px;
}
</style>
