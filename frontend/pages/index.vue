<script setup>
definePageMeta({
  layout: false,
});

const router = useRouter();
const formData = ref({
  identify: '',
  password: '',
});
async function login() {
  // 유효성 체크
  // post
  const response = { code: 0, result: true, msg: '' };
  const { result } = response;
  result ? loginSuccess() : loginFail();
}

function loginSuccess() {
  // 토큰 관련
  router.push('/ai_search');
}

function loginFail(msg) {
  // toast msg
}
</script>
<template>
  <div id="LoginPage">
    <div class="gradient-bg">
      <svg xmlns="http://www.w3.org/2000/svg">
        <defs>
          <filter id="goo">
            <feGaussianBlur
              in="SourceGraphic"
              stdDeviation="10"
              result="blur"
            />
            <feColorMatrix
              in="blur"
              mode="matrix"
              values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -8"
              result="goo"
            />
            <feBlend in="SourceGraphic" in2="goo" />
          </filter>
        </defs>
      </svg>
      <div class="gradients-container">
        <div class="g1"></div>
        <div class="g2"></div>
        <div class="g3"></div>
        <div class="g4"></div>
        <div class="g5"></div>
        <div class="interactive"></div>
      </div>
    </div>
    <div class="login_left">
      <div>
        <h2 class="fw-700 dotum">환영합니다!</h2>
        <p class="title--l dotum fw-700">
          <span class="buri mr-1">AmoreSearch</span>와 함께하는 더 나은 내일
        </p>
        <p class="mt-3 mb-4 dotum">
          <span class="dotum">우리 회사의 업무를 지원하고,</span>
          <br />
          <span class="dotum"
            >화장품 산업에서 중요한 혁신을 이끌어가도록 돕겠습니다.</span
          >
        </p>
        <p class="title--m fw-600 mt-12">
          로그인하고 효율적인 업무 시작하세요!
        </p>
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
          <v-btn class="w-full" color="main" @click="login">로그인</v-btn>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
#LoginPage {
  display: flex;
  height: 100vh;
}
#LoginPage h2 {
  font-size: 3.75rem;
  line-height: 5rem;
  opacity: 0;
  animation: fadeInDown 1.5s forwards;
}
.login_left > div p:nth-of-type(1) {
  font-size: 1.75rem;
  line-height: 34px;
  opacity: 0;
  animation: fadeInDown 1.5s forwards;
  animation-delay: 0.05s;
}
.login_left > div p:nth-of-type(2) {
  opacity: 0;
  animation: fadeInDown 1.5s forwards;
  animation-delay: 0.1s;
}
.login_left > div p:nth-of-type(3) {
  opacity: 0;
  animation: fadeInDown 1.5s forwards;
  animation-delay: 0.15s;
}
.login_left,
.login_right {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-width: 700px;
  z-index: 1;
}
.login_left {
  width: 52%;
  color: white;
}

.login_left > div {
  min-width: 460px;
}
.login_right {
  width: 48%;
  align-items: center;
}
.login_form {
  width: 280px;
}

.gradient-bg {
  width: 52%;
  min-width: 700px;
  height: 100vh;
  position: fixed;
  overflow: hidden;
  background: linear-gradient(40deg, var(--color-bg1), var(--color-bg2));
  top: 0;
  left: 0;

  svg {
    position: fixed;
    top: 0;
    left: 0;
    width: 0;
    height: 0;
  }

  .gradients-container {
    filter: url(#goo) blur(40px);
    width: 100%;
    height: 100%;
  }

  .g1 {
    position: absolute;
    background: radial-gradient(
        circle at center,
        rgba(var(--color1), 0.8) 0,
        rgba(var(--color1), 0) 50%
      )
      no-repeat;
    mix-blend-mode: var(--blending);

    width: var(--circle-size);
    height: var(--circle-size);
    top: calc(50% - var(--circle-size) / 2);
    left: calc(50% - var(--circle-size) / 2);

    transform-origin: center center;
    animation: moveVertical 30s ease infinite;

    opacity: 1;
  }

  .g2 {
    position: absolute;
    background: radial-gradient(
        circle at center,
        rgba(var(--color2), 0.8) 0,
        rgba(var(--color2), 0) 50%
      )
      no-repeat;
    mix-blend-mode: var(--blending);

    width: var(--circle-size);
    height: var(--circle-size);
    top: calc(50% - var(--circle-size) / 2);
    left: calc(50% - var(--circle-size) / 2);

    transform-origin: calc(50% - 400px);
    animation: moveInCircle 20s reverse infinite;

    opacity: 1;
  }

  .g3 {
    position: absolute;
    background: radial-gradient(
        circle at center,
        rgba(var(--color3), 0.8) 0,
        rgba(var(--color3), 0) 50%
      )
      no-repeat;
    mix-blend-mode: var(--blending);

    width: var(--circle-size);
    height: var(--circle-size);
    top: calc(50% - var(--circle-size) / 2 + 200px);
    left: calc(50% - var(--circle-size) / 2 - 500px);

    transform-origin: calc(50% + 400px);
    animation: moveInCircle 40s linear infinite;

    opacity: 1;
  }

  .g4 {
    position: absolute;
    background: radial-gradient(
        circle at center,
        rgba(var(--color4), 0.8) 0,
        rgba(var(--color4), 0) 50%
      )
      no-repeat;
    mix-blend-mode: var(--blending);

    width: var(--circle-size);
    height: var(--circle-size);
    top: calc(50% - var(--circle-size) / 2);
    left: calc(50% - var(--circle-size) / 2);

    transform-origin: calc(50% - 200px);
    animation: moveHorizontal 40s ease infinite;

    opacity: 0.7;
  }

  .g5 {
    position: absolute;
    background: radial-gradient(
        circle at center,
        rgba(var(--color5), 0.8) 0,
        rgba(var(--color5), 0) 50%
      )
      no-repeat;
    mix-blend-mode: var(--blending);

    width: calc(var(--circle-size) * 2);
    height: calc(var(--circle-size) * 2);
    top: calc(50% - var(--circle-size));
    left: calc(50% - var(--circle-size));

    transform-origin: calc(50% - 800px) calc(50% + 200px);
    animation: moveInCircle 20s ease infinite;

    opacity: 1;
  }

  .interactive {
    position: absolute;
    background: radial-gradient(
        circle at center,
        rgba(var(--color-interactive), 0.8) 0,
        rgba(var(--color-interactive), 0) 50%
      )
      no-repeat;
    mix-blend-mode: var(--blending);

    width: 100%;
    height: 100%;
    top: -50%;
    left: -50%;

    opacity: 0.7;
  }
}
</style>
