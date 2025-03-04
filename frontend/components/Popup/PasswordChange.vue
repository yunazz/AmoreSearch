<script setup>
const props = defineProps({});
const emit = defineEmits(["submit", "close"]);

const form = ref({
  password: "",
  new_password: "",
  new_password_check: "",
});
const snackbar = ref({ active: false, message: "" });

const notify = (msg) => {
  snackbar.value.message = msg;
  snackbar.value.active = true;
  return false;
};

const validatePassword = () => {
  snackbar.value.active = false;
  const { password, new_password, new_password_check } = form.value;

  if (password.length === 0) return notify("현재 비밀번호를 입력해 주세요.");
  if (new_password.length === 0) return notify("비밀번호를 입력해 주세요.");
  if (new_password_check.length === 0)
    return notify("비밀번호 확인을 입력해 주세요.");
  if (new_password !== new_password_check)
    return notify("비밀번호가 일치하지 않습니다.");

  return true;
};

async function updateMyPassword() {
  if (!validatePassword()) return;
  const { code, msg } = await $http("/auth/member/password", {
    method: "PUT",
    body: {
      password: form.password,
      new_password: form.new_password,
      new_password_check: form.new_password_check,
    },
  });

  // if (false) {
  //   return notify("현재 비밀번호가 틀렸습니다.비밀번호를 확인해 주세요.");
  // }
  // notify(msg);
  // if (code == 0) emit("submit");
}
</script>

<template>
  <v-dialog v-model="$attrs" max-width="390">
    <v-card class="board_card">
      <v-toolbar align="center" color="black" class="px-7">
        비밀번호 변경
      </v-toolbar>
      <v-card-text class="mt-2">
        <form onsubmit="return false;">
          <div class="input_cont">
            <label> 현재 비밀번호 </label>
            <v-text-field
              hide-details
              variant="outlined"
              v-model="form.password"
              type="password"
              autocomplete="off"
            />
          </div>
          <div class="input_cont">
            <label> 비밀번호 </label>
            <v-text-field
              hide-details
              variant="outlined"
              v-model="form.new_password"
              type="password"
              autocomplete="off"
            />
          </div>
          <div class="input_cont">
            <label> 비밀번호 확인 </label>
            <v-text-field
              hide-details
              variant="outlined"
              v-model="form.new_password_check"
              type="password"
              autocomplete="off"
            />
          </div>
        </form>
      </v-card-text>
      <v-card-actions class="pt-4 pb-3 px-6 border-top-1">
        <div class="flex justify-center gap-2">
          <v-btn
            variant="flat"
            color="black"
            text
            width="80"
            @click="updateMyPassword"
          >
            변경
          </v-btn>
          <v-btn
            variant="outlined"
            color="gray-black"
            text
            width="80"
            @click="emit('close')"
          >
            취소
          </v-btn>
        </div>
      </v-card-actions>
      <v-snackbar v-model="snackbar.active" :timeout="3000" color="primary">
        {{ snackbar.message }}
      </v-snackbar>
    </v-card>
  </v-dialog>
</template>
