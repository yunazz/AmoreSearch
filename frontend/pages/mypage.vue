<script setup>
const member = useMember();
// tab
const tab = ref("INFO");
const tabItems = ref([
  { text: "회원정보 수정", value: "INFO" },
  { text: "비밀번호 수정", value: "PASSWORD" },
]);

// form
const form = ref({
  phone: member.value.phone,
});
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
  if (password.length > 0) return notify("현재 비밀번호를 입력해 주세요.");
  if (new_password.length > 0)
    return notify("새로운 비밀번호를 입력해 주세요.");
  if (new_password_check.length > 0)
    return notify("새로운 비밀번호 확인을 입력해 주세요.");
  if (new_password_check.length !== new_password_check)
    return notify("새로운 비밀번호 확인을 입력해 주세요.");

  if (false) {
    return notify("잘못 입력되었습니다.현재 비밀번호를 확인해해 주세요.");
  }

  return true;
};

async function updateMyInfo() {
  if (!validatePhone(form.value.phone))
    return notify("휴대폰번호를 확인해 주세요.");

  console.log("update!!");
}

async function updateMyPassword() {
  if (!validatePassword()) return;

  console.log("update!!");
}
</script>

<template>
  <div id="Mypage" class="content">
    <div class="content_inner">
      <div class="page_header">
        <h2 class="page_title">마이페이지</h2>
        <ClientOnly>
          <v-tabs
            class="tab_narrow mb-4"
            v-model="tab"
            bg-color="transparent"
            align-tabs="center"
          >
            <v-tab
              v-for="item in tabItems"
              :key="item.value"
              :text="item.text"
              :value="item.value"
            ></v-tab>
          </v-tabs>
        </ClientOnly>
      </div>

      <article class="tab_content" v-if="tab == 'INFO'">
        <div>
          <div class="input_cont">
            <label>사원번호</label>
            <v-text-field
              hide-details
              density="compact"
              variant="underlined"
              v-model="member.emp_no"
              maxLength="10"
              disabled
              readonly
            />
          </div>
          <div class="input_cont">
            <label>이름</label>
            <v-text-field
              hide-details
              density="compact"
              variant="underlined"
              v-model="member.name"
              maxLength="20"
              disabled
              readonly
            />
          </div>

          <div class="input_cont">
            <label class="text-main">
              휴대폰번호 <b class="text-main ml-1">*</b>
            </label>
            <v-text-field
              hide-details
              variant="underlined"
              v-model="form.phone"
              v-mask="'###-####-####'"
            />
          </div>
          <div class="input_cont mb-3">
            <label>생년월일</label>
            <v-text-field
              hide-details
              density="compact"
              variant="underlined"
              v-model="member.birth_date"
              maxLength="10"
              disabled
              v-mask="'####-##-##'"
              readonly
            />
          </div>
          <div class="input_cont mb-3">
            <label>입사일</label>
            <v-text-field
              hide-details
              density="compact"
              variant="underlined"
              v-model="member.hire_date"
              maxLength="10"
              disabled
              v-mask="'####-##-##'"
              readonly
            />
          </div>
          <div class="input_cont mb-3">
            <label>소속</label>
            <v-text-field
              hide-details
              variant="underlined"
              v-model="member.company_affiliation"
              single-line
              disabled
            />
          </div>
          <div class="input_cont mb-3">
            <label>근무부서</label>
            <v-text-field
              hide-details
              variant="underlined"
              v-model="member.department"
              single-line
              disabled
            />
          </div>
          <div class="input_cont mb-3">
            <label>직급</label>
            <v-text-field
              hide-details
              variant="underlined"
              v-model="member.position"
              single-line
              disabled
            />
          </div>
        </div>
      </article>

      <article class="tab_content" v-if="tab == 'PASSWORD'">
        <div>
          <div class="input_cont">
            <label> 현재 비밀번호 </label>
            <v-text-field
              hide-details
              variant="underlined"
              v-model="passwordForm.password"
            />
          </div>
          <div class="input_cont">
            <label> 새로운 비밀번호 </label>
            <v-text-field
              hide-details
              variant="underlined"
              v-model="passwordForm.new_password"
            />
          </div>
          <div class="input_cont mb-6">
            <label> 새로운 비밀번호 확인 </label>
            <v-text-field
              hide-details
              variant="underlined"
              v-model="passwordForm.new_password_check"
            />
          </div>
        </div>
      </article>
      <div class="flex justify-center">
        <v-btn
          v-if="tab === 'INFO'"
          width="90"
          color="main"
          @click="updateMyInfo"
          >수정</v-btn
        >
      </div>
      <div class="flex justify-center">
        <v-btn
          v-if="tab === 'PASSWORD'"
          width="136"
          color="main"
          @click="updateMyPassword"
          >비밀번호 수정</v-btn
        >
      </div>
      <v-snackbar v-model="snackbar" :timeout="3000" color="main">
        {{ message }}
        <template v-slot:action="{ attrs }">
          <v-btn color="red" text v-bind="attrs" @click="snackbar = false">
            닫기
          </v-btn>
        </template>
      </v-snackbar>
    </div>
  </div>
</template>

<style scoped>
article {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  margin: 1.5rem 0 2.25rem;
}
article > div {
  /* border: 1px solid var(--border-color); */
  padding: 32px 40px 16px;
  display: flex;
  flex-direction: column;
  row-gap: 0.625rem;
  width: 430px;
  border-radius: 16px;
  box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
}
.input_cont {
  display: flex;
  flex-direction: row;
  align-items: center;
  column-gap: 1.5rem;
  font-weight: 500;
}
.tab_content .input_cont label {
  font-size: 0.875rem;
}

.tab_content:nth-child(1) .input_cont label {
  width: 90px;
}
.tab_content:nth-child(2) .input_cont label {
  width: 130px;
}
</style>
