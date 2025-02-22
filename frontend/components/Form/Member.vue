<script setup>
const props = defineProps(["mode", "item"]);
const emit = defineEmits(["submit", "close"]);

const form = ref({
  role: 1,
  emp_no: "",
  name: "",
  password: "",
  department: "",
  position: "",
  birth_date: "",
  hire_date: "",
  phone: "",
  resign_date: "",
  resign_reason: "",
});

const initFormData = () => {
  if (props.mode === "register") {
  } else if (props.mode === "edit") {
    form.value = {
      ...props.item,
      password: "",
      resign_date: "",
      resign_reason: "",
    };
  } else if (props.mode === "info") {
    form.value = { ...props.item };
  }
};

const valid = ref(false);
// Date picker 관련
const menu_birth = ref(false);
const menu_hire = ref(false);
const menu_resign = ref(false);
const datepicker_birth = ref(null);
const datepicker_hire = ref(null);
const datepicker_resign = ref(null);

const close = () => {
  emit("close", props.mode);
};

const submit = () => {
  emit("submit", props.mode, form);
  close();
};

onMounted(() => {
  initFormData();
});
</script>

<template>
  <v-card>
    <v-toolbar align="center" color="black" class="px-7">
      <v-icon icon="mdi-account" class="mr-3 title--l" />
      직원 {{ mode === "register" ? "등록" : mode === "edit" && "수정" }}
    </v-toolbar>
    <v-card-text>
      <v-form v-model="valid" class="px-3">
        <div class="input_cont flex align-center">
          <label class="mr-4">권한</label>
          <v-chip-group
            v-model="form.role"
            selected-class="text-deep-purple-accent-4"
            mandatory
          >
            <v-chip variant="outlined" :value="2">관리자</v-chip>
            <v-chip variant="outlined" :value="1">일반</v-chip>
          </v-chip-group>
        </div>
        <div class="grid-cols-2">
          <div class="input_cont">
            <label>사원번호</label>
            <v-text-field
              density="compact"
              variant="outlined"
              v-model="form.emp_no"
              placeholder="사원번호 10자리를 입력해주세요"
              :rules="[
                (v) =>
                  v.length == 0 || v.length == 10 || '10자리를 입력해주세요',
              ]"
              oninput="javascript: this.value = this.value.replace(/[^0-9]/g, '');"
              maxLength="10"
            />
          </div>
          <div class="input_cont">
            <label>이름</label>
            <v-text-field
              density="compact"
              variant="outlined"
              v-model="form.name"
              placeholder="20자 이내로 입력해주세요"
              :rules="[(v) => v.length <= 20 || '20자 이내로 입력해주세요']"
              maxLength="20"
            />
          </div>
        </div>

        <div class="grid-cols-2">
          <div class="input_cont">
            <label>비밀번호</label>
            <v-text-field
              density="compact"
              variant="outlined"
              v-model="form.password"
              type="password"
              autocomplete="off"
              placeholder="20자 이내로 입력해주세요"
              :rules="[(v) => v.length <= 20 || '20자 이내로 입력해주세요']"
              maxLength="20"
            />
          </div>
          <div class="input_cont">
            <label>휴대폰번호</label>
            <v-text-field
              hide-details
              density="compact"
              variant="outlined"
              v-model="form.phone"
              v-mask="'###-####-####'"
            />
          </div>
        </div>
        <div class="grid-cols-2">
          <client-only>
            <div class="input_cont mb-3">
              <label>생년월일</label>
              <v-text-field
                hide-details
                density="compact"
                variant="outlined"
                v-model="form.birth_date"
                v-mask="'####-##-##'"
                prepend-inner-icon="mdi-calendar"
                readonly
              >
                <v-menu
                  v-model="menu_birth"
                  :close-on-content-click="false"
                  activator="parent"
                  width="200"
                >
                  <v-date-picker
                    hide-header
                    show-adjacent-months
                    v-model="datepicker_birth"
                    @update:modelValue="form.birth_date = formatDate($event)"
                  />
                </v-menu>
              </v-text-field>
            </div>
            <div class="input_cont mb-3">
              <label>입사일</label>
              <v-text-field
                hide-details
                density="compact"
                variant="outlined"
                v-model="form.hire_date"
                v-mask="'####-##-##'"
                prepend-inner-icon="mdi-calendar"
                readonly
              >
                <v-menu
                  v-model="menu_hire"
                  :close-on-content-click="false"
                  activator="parent"
                >
                  <v-date-picker
                    hide-header
                    show-adjacent-months
                    v-model="datepicker_hire"
                    @update:modelValue="form.hire_date = formatDate($event)"
                  />
                </v-menu>
              </v-text-field>
            </div>
          </client-only>
        </div>
        <div class="grid-cols-2">
          <div class="input_cont mb-3">
            <label>근무부서</label>
            <v-select
              hide-details
              variant="outlined"
              v-model="form.department"
              :items="enums.departments"
              single-line
            />
          </div>
          <div class="input_cont mb-3">
            <label>직급</label>
            <v-select
              hide-details
              variant="outlined"
              v-model="form.position"
              :items="enums.positions"
              single-line
            />
          </div>
        </div>
        <v-divider class="mt-4 mb-4" />

        <div class="grid-cols-2">
          <client-only>
            <div class="input_cont mb-3">
              <label>퇴사일</label>
              <v-text-field
                hide-details
                density="compact"
                variant="outlined"
                v-model="form.resign_date"
                v-mask="'####-##-##'"
                :rules="[
                  (v) =>
                    !v ||
                    /^\d{4}-\d{2}-\d{2}$/.test(v) ||
                    'YYYY-MM-DD 형식으로 입력해주세요',
                ]"
                prepend-inner-icon="mdi-calendar"
                readonly
              >
                <v-menu
                  v-model="menu_resign"
                  :close-on-content-click="false"
                  activator="parent"
                >
                  <v-date-picker
                    hide-header
                    show-adjacent-months
                    v-model="datepicker_resign"
                    @update:modelValue="form.resign_date = formatDate($event)"
                  />
                </v-menu>
              </v-text-field>
            </div>
          </client-only>
        </div>

        <div class="input_cont">
          <label>퇴사사유</label>
          <v-textarea row-height="25" rows="5" variant="outlined" auto-grow />
        </div>
      </v-form>
    </v-card-text>

    <v-card-actions class="pt-4 pb-3 border-top-1">
      <v-btn
        size="large"
        variant="flat"
        color="black"
        text
        width="90"
        @click="submit"
        >저장</v-btn
      >
      <v-btn
        size="large"
        variant="outlined"
        color="grey-black"
        text
        width="90"
        @click="close"
        >취소</v-btn
      >
    </v-card-actions>
  </v-card>
</template>
<style scoped>
.input_cont {
}
.input_cont label {
  color: var(--color-grey-05);
  display: inline-block;
  font-size: 0.8125rem;
  margin-bottom: 4px;
}
</style>
