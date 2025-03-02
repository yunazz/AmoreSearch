<script setup>
const props = defineProps({});
const emit = defineEmits(["submit", "close"]);

const passwordForm = ref({
  password: "",
  new_password: "",
  new_password_check: "",
});
// snackbar
const snackbar = ref(false);
const message = ref("");

const notify = (msg) => {
  message.value = msg;
  snackbar.value = true;
  return false;
};

const validatePassword = () => {
  const { password, new_password, new_password_check } = passwordForm.value;

  if (password.length === 0) return notify("현재 비밀번호를 입력해 주세요.");
  if (new_password.length === 0) return notify("비밀번호를 입력해 주세요.");
  if (new_password_check.length === 0)
    return notify("비밀번호 확인을 입력해 주세요.");
  if (new_password_check.length !== new_password_check)
    return notify("비밀번호가 일치하지 않습니다.");

  if (false) {
    return notify("현재 비밀번호가 틀렸습니다.비밀번호를 확인해 주세요.");
  }

  return true;
};

async function updateMyPassword() {
  if (!validatePassword()) return;

  console.log("updateMyPassword!!");
}
</script>

<template>
  <v-dialog v-model="$attrs" max-width="390">
    <v-card class="board_card">
      <v-toolbar align="center" color="black" class="px-7">
        비밀번호 변경
      </v-toolbar>
      <v-card-text class="mt-2">
        <div class="input_cont">
          <label> 현재 비밀번호 </label>
          <v-text-field
            hide-details
            variant="outlined"
            v-model="passwordForm.password"
          />
        </div>
        <div class="input_cont">
          <label> 비밀번호 </label>
          <v-text-field
            hide-details
            variant="outlined"
            v-model="passwordForm.new_password"
          />
        </div>
        <div class="input_cont">
          <label> 비밀번호 확인 </label>
          <v-text-field
            hide-details
            variant="outlined"
            v-model="passwordForm.new_password_check"
          />
        </div>
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
      <Snackbar v-model="snackbar" :message="message" />
    </v-card>
  </v-dialog>
</template>
