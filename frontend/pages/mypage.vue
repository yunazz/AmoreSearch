<script setup>
const member = useMember();
const dialogPwdChange = ref(false);
const dialogConfirm = ref({
  active: false,
  title: "",
  text: "",
});
const snackbar = ref({ active: false, message: "" });

const form = ref({
  phone: member.value.phone,
});

async function updateMyInfo() {
  dialogConfirm.value.active = false;

  if (!validatePhone(form.value.phone))
    return notify("휴대폰번호를 확인해 주세요.");

  const { code, msg, result } = await $http("/member/me", {
    method: "PUT",
    body: {
      member_id: member.value.member_id,
      phone: form.value.phone.replaceAll("-", ""),
    },
  });

  snackbar.value.active = true;
  if (code == 1) return (snackbar.value.message = msg);

  snackbar.value.message = "수정되었습니다.";
}
</script>

<template>
  <div id="Mypage" class="content">
    <div class="content_inner">
      <div class="page_header">
        <h2 class="page_title">마이페이지</h2>
      </div>
      <div id="myInfo" class="flex">
        <div>
          <h3>
            <v-icon
              v-if="member.role == 2"
              icon="mdi-shield-account"
              color="primary"
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
          <h4><v-icon icon="mdi-smart-card-outline" class="mr-3" />회원정보</h4>
          <v-divider class="mt-2 mb-2" thickness="2" opacity=".8" />

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
                    color="black"
                    @click="
                      activate_confirm(
                        dialogConfirm,
                        '회원정보 수정',
                        '수정하시겠습니까?'
                      )
                    "
                  >
                    수정
                  </v-btn>
                </div>
              </div>
            </div>
          </article>
          <article class="my-setting">
            <h5></h5>
            <v-divider thickness="2" opacity=".8" />
            <div>
              <p><small class="mr-2">▶</small> 비밀번호 변경</p>
              <p>
                <v-btn
                  @click="dialogPwdChange = true"
                  color="primary"
                  width="160"
                  rounded
                  variant="outlined"
                >
                  <v-icon icon="mdi-lock-outline " class="mr-2" />
                  비밀번호 변경
                </v-btn>
              </p>
            </div>
          </article>
        </section>
      </div>
    </div>

    <v-snackbar v-model="snackbar.active" :timeout="3000" color="primary">
      {{ snackbar.message }}
    </v-snackbar>
    <!-- DIALOG -->
    <PopupPasswordChange
      v-model="dialogPwdChange"
      @close="dialogPwdChange = false"
    />

    <PopupConfirm
      v-model="dialogConfirm.active"
      :title="dialogConfirm.title"
      :text="dialogConfirm.text"
      @submit="updateMyInfo"
      @close="dialogConfirm.active = false"
    />
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
  color: var(--color-black);
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
  height: 76px;
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
  color: var(--color-black);
}

#passwordChange {
  width: 100%;
}
#passwordChange .input_cont label {
  width: 120px;
}
</style>
