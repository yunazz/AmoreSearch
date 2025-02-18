<script setup>
// const router = useRouter();
const formData = ref({});

async function login() {
  // 유효성 체크
  // post
  const response = { code: 0, result: true, msg: "" };
  const { result, msg } = response;
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
  <div></div>
</template>

<style scoped></style>
