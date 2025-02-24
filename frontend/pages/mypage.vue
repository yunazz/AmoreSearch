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
  console.log(password);
  console.log(new_password);
  console.log(new_password_check);
  if (password.length === 0) return notify("현재 비밀번호를 입력해 주세요.");
  if (new_password.length === 0) return notify("비밀번호를 입력해 주세요.");
  if (new_password_check.length === 0)
    return notify("비밀번호 확인을 입력해 주세요.");
  if (new_password_check.length !== new_password_check)
    return notify("비밀번호가 일치하지 않습니다.");

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
      <template v-if="tab == 'INFO'">
        <div id="myInfo" class="flex">
          <div>
            <h3>
              <v-icon
                v-if="member.role == 2"
                icon="mdi-shield-account"
                color="main"
                class="mr-2 mb-2"
              />
              <span> {{ member.name }} </span>
            </h3>
            <v-divider class="mb-2" thickness="2" />
            <div class="info_summary px-1">
              <p><span>권한</span>{{ enums.roles[member.role] }}</p>
              <p><span>사원번호</span>{{ member.emp_no }}</p>
              <p><span>입사일</span>{{ member.hire_date }}</p>
            </div>
            <v-divider class="mt-2" thickness="2" />
          </div>

          <section class="info_detail">
            <h4>
              <v-icon icon="mdi-smart-card-outline" class="mr-3" />회원정보
            </h4>
            <v-divider class="mt-2 mb-2" thickness="2" opacity="1" />

            <article>
              <h5><small class="mr-2">▶</small>직원정보</h5>
              <div class="grid-cols-2">
                <p>
                  <span>직급</span>
                  <span>{{ member.position }}</span>
                </p>
                <p>
                  <span>소속/부서</span>
                  <span>
                    {{ member.company_affiliation }} /
                    {{ member.department }}
                  </span>
                </p>
              </div>
            </article>
            <v-divider class="mt-4 mb-5" />

            <article class="mb-6">
              <h5><small class="mr-2">▶</small> 개인정보</h5>
              <div class="grid-cols-2">
                <p>
                  <span>생년월일</span>
                  <span>{{ member.birth_date }}</span>
                </p>
                <div class="input_cont">
                  <label> 휴대폰번호 </label>
                  <div class="flex gap-2">
                    <v-text-field
                      width="184"
                      hide-details
                      variant="outlined"
                      v-model="form.phone"
                      v-mask="'###-####-####'"
                    />
                    <v-btn
                      width="70"
                      v-if="tab === 'INFO'"
                      color="black"
                      @click="updateMyInfo"
                    >
                      수정
                    </v-btn>
                  </div>
                </div>
              </div>
            </article>
            <article class="my-setting">
              <v-divider thickness="2" opacity="1" />
              <div>
                <p>비밀번호 변경</p>
                <p>
                  <v-btn @click="dialog = true" color="main" width="140px">
                    <v-icon icon="mdi-lock-outline " class="mr-3" />
                    비밀번호 변경
                  </v-btn>
                </p>
              </div>
            </article>
            <v-divider thickness="2" opacity="1" />
          </section>
        </div>
      </template>
    </div>
    <!-- DIALOG -->
    <v-dialog v-model="dialog" max-width="390">
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
              @click="dialog = false"
            >
              취소
            </v-btn>
          </div>
        </v-card-actions>
        <v-snackbar v-model="snackbar" :timeout="3000" color="main">
          {{ message }}
        </v-snackbar>
      </v-card>
    </v-dialog>
  </div>
</template>

<style scoped>
.v-snackbar__wrapper {
  margin-left: 200px;
}

#myInfo {
  display: flex;
  /* flex-direction: column; */
  width: 1000px;
  margin: 1.5rem auto 2.25rem;
  column-gap: 2.75rem;
}
#myInfo h3 {
  font-size: var(--body-size-l) !important;
  font-weight: 600;
  margin: 0 auto;
  color: black;
}
#myInfo .info_summary {
  display: flex;
  flex-direction: column;
  width: 200px;
  font-size: var(--body-size-m) !important;
  margin-top: 14px;
}
#myInfo .info_summary p {
  display: flex;
  justify-content: space-between;
  padding: 0 12px;
  height: 28px;
}
#myInfo .info_summary p span:nth-of-type(1) {
  width: 76px;
  font-size: 0.8125rem;
  font-weight: 400;
  color: var(--color-gray-04);
  font-weight: 500;
}

#myInfo .info_detail {
  width: calc(100% - 200px);
}
#myInfo .info_detail .input_cont {
  display: flex;
  flex-direction: row;
  align-items: center;
  column-gap: 1.5rem;
  font-weight: 500;
}
#myInfo .info_detail .input_cont label {
  color: var(--color-gray-04);
  font-size: 0.8125rem;
  width: 64px;
  font-weight: 400;
}
#myInfo h4 {
  font-size: var(--title-size-m);
  margin-bottom: 6px;
}
#myInfo h5 {
  font-size: var(--title-size-s);
  display: flex;
  align-items: center;
  margin-top: 20px;
  margin-bottom: 8px;
  font-weight: 600;
}

article.my-setting {
  margin-top: 70px;
}
article.my-setting > div {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 80px;
  padding: 0 20px;
}
article.my-setting p {
  font-weight: 500;
}
#myInfo .info_detail p {
  display: flex;
  align-items: center;
  height: 36px;
}
#myInfo p span:nth-of-type(1) {
  width: 86px;
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
