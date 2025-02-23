<script setup>
const member = useMember();
const dialog = ref(false);

// tab
const tab = ref("INFO");
const tabItems = ref([
  { text: "회원 정보", value: "INFO" },
  // { text: "비밀번호 변경", value: "PASSWORD" },
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
  if (new_password.length > 0) return notify("비밀번호를 입력해 주세요.");
  if (new_password_check.length > 0)
    return notify("비밀번호 확인을 입력해 주세요.");
  if (new_password_check.length !== new_password_check)
    return notify("비밀번호 확인을 입력해 주세요.");

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
          <!-- <v-tabs
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
          </v-tabs> -->
        </ClientOnly>
      </div>

      <article v-if="tab == 'INFO'" id="myInfo" class="tab_content">
        <div>
          <h4 class="px-3">
            <span>
              {{ member.name }}
            </span>
            <v-icon
              v-if="member.role == 2"
              icon="mdi-shield-account"
              color="main"
              class="ml-1 mb-2"
            />
          </h4>
          <v-divider class="mb-2" />
          <div class="flex gap-4">
            <div>
              <h5>
                <v-icon icon="mdi-smart-card-outline" class="mr-2" />직원정보
              </h5>
              <p>
                <span>직급</span>
                <span>{{ member.position }}</span>
              </p>
              <p>
                <span>사원번호</span>
                <span>{{ member.emp_no }}</span>
              </p>
              <p>
                <span>소속/부서</span>
                <span
                  >{{ member.company_affiliation }} / {{ member.department }}
                </span>
              </p>
              <p>
                <span>입사일</span>
                <span>{{ member.hire_date }}</span>
              </p>
            </div>
            <div>
              <!-- <v-divider class="my-2" /> -->
              <h5><v-icon icon="mdi-lock-outline" class="mr-2" />개인정보</h5>
              <p>
                <span>생년월일</span>
                <span>{{ member.birth_date }}</span>
              </p>
              <div class="input_cont">
                <label style="min-width: 60px"> 휴대폰번호 </label>
                <div class="flex gap-2 w-100">
                  <v-text-field
                    hide-details
                    variant="outlined"
                    v-model="form.phone"
                    v-mask="'###-####-####'"
                  />
                  <v-btn
                    v-if="tab === 'INFO'"
                    color="black"
                    @click="updateMyInfo"
                  >
                    수정
                  </v-btn>
                </div>
              </div>
              <p class="mt-2">
                <span>비밀번호</span>
                <v-btn @click="dialog = true" color="black"
                  >비밀번호 변경</v-btn
                >
              </p>
            </div>
          </div>
        </div>
      </article>
    </div>
    <v-dialog v-model="dialog" max-width="390">
      <v-card class="board_card">
        <v-toolbar align="center" color="black" class="px-7">
          비밀번호 변경
        </v-toolbar>
        <v-card-text class="mt-2">
          <div id="passwordChange" class="tab_content">
            <div>
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
            </div>
          </div>
        </v-card-text>
        <v-card-actions class="pt-4 pb-3 px-6 border-top-1">
          <div class="flex justify-center">
            <v-btn
              variant="flat"
              color="black"
              text
              width="80"
              @click="updateMyPassword"
            >
              변경
            </v-btn>
          </div>
        </v-card-actions>
        <v-snackbar v-model="snackbar" :timeout="3000" color="main">
          {{ message }}
          <template v-slot:action="{ attrs }">
            <v-btn color="red" text v-bind="attrs" @click="snackbar = false">
              닫기
            </v-btn>
          </template>
        </v-snackbar>
      </v-card>
    </v-dialog>
  </div>
</template>

<style scoped>
#Mypage span,
#Mypage .input_cont div.v-field__input,
#Mypage .input_cont input.v-field__input,
#Mypage .input_cont input.v-field__input::placeholder {
}

.v-snackbar__wrapper {
  margin-left: 200px;
}

article {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  margin: 1.5rem 0 2.25rem;
}
.tab_content > div {
  display: flex;
  flex-direction: column;
  row-gap: 0.625rem;
  border-radius: 16px;
}
.tab_content .input_cont {
  display: flex;
  flex-direction: row;
  align-items: center;
  column-gap: 1.5rem;
  font-weight: 500;
}
.tab_content .input_cont label {
  font-size: 0.875rem;
}
#myInfo > div {
  width: 740px;
  padding: 10px 40px 30px;
  padding-bottom: 30px;
}
#myInfo .flex.gap-4 > div {
  padding: 0 12px;
}
#myInfo .flex.gap-4 > div:first-of-type {
  width: 47%;
}
#myInfo .flex.gap-4 > div:last-of-type {
  width: 53%;
}
#myInfo h4 {
  font-size: 1rem !important;
  font-weight: 500;
  color: black;
}
#myInfo h5 {
  margin-bottom: 7px;
  font-size: 0.875rem;
  font-weight: 600;
}
#myInfo p {
  display: flex;
  align-items: center;
  height: 40px;
}
#Mypage label {
  font-size: 0.8125rem;
  color: var(--color-gray-04);
}
#myInfo p span:nth-of-type(1) {
  width: 67px;
  margin-right: 16px;
  font-size: 0.8125rem;
  color: var(--color-gray-04);
}
#myInfo p span:nth-of-type(2) {
  font-size: 0.875rem;
  color: black;
}

#passwordChange {
  width: 100%;
}
#passwordChange .input_cont label {
  width: 120px;
}
</style>
