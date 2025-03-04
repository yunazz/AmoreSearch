<script setup>
const member = useMember();
const props = defineProps({
  dialog: { type: Boolean },
  mode: { type: String },
  item: {
    type: Object,
    default: {
      role: 1,
      emp_no: "",
      name: "",
      company_affiliation: "",
      department: "",
      position: "사원",
      birth_date: "",
      phone: "",
      hire_date: "",
      employment_status: "재직",
      resign_date: "",
      resign_reason: "",
    },
  },
});
const emit = defineEmits(["submit", "close"]);
const modeText = computed(() => {
  if (props.mode === "register") return "등록";
  if (props.mode === "edit") return "수정";
});
const isDisabled = computed(
  () => props.item?.employment_status === "퇴직" && member.role !== 3
);
const form = ref({ ...props.item, password: "" });

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
function initResignOptions() {
  if (form.value.employment_status !== "퇴직") {
    form.value.resign_date = "";
    form.value.resign_reason = "";
    datepicker_resign = null;
  }
}
</script>

<template>
  <v-dialog v-model="$attrs" max-width="560" scrollable>
    <v-card>
      <v-toolbar align="center" color="black" class="px-7">
        직원 {{ modeText }}
      </v-toolbar>
      <v-card-text>
        <v-form v-model="valid" class="pt-2">
          <div class="input_cont flex align-center" v-if="member.role >= 2">
            <label class="mr-4">권한</label>
            <v-chip-group
              v-model="form.role"
              mandatory
              selected-class="chip-selected"
            >
              <v-chip color="grey-lighten-2" :value="2" :disabled="isDisabled"
                >관리자</v-chip
              >
              <v-chip color="grey-lighten-2" :value="1" :disabled="isDisabled"
                >일반</v-chip
              >
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
                :disabled="isDisabled"
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
                :disabled="isDisabled"
              />
            </div>
          </div>

          <div class="grid-cols-2">
            <div class="input_cont">
              <label>{{ mode === "edit" ? "초기화 " : "" }}비밀번호</label>
              <v-text-field
                density="compact"
                variant="outlined"
                v-model="form.password"
                type="password"
                autocomplete="off"
                placeholder="20자 이내로 입력해주세요"
                :rules="[(v) => v.length <= 20 || '20자 이내로 입력해주세요']"
                maxLength="20"
                :disabled="isDisabled"
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
                :disabled="isDisabled"
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
                  :disabled="isDisabled"
                  readonly
                >
                  <v-menu
                    v-model="menu_birth"
                    :close-on-content-click="false"
                    activator="parent"
                    width="200"
                    :disabled="isDisabled"
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
                  :disabled="isDisabled"
                  readonly
                >
                  <v-menu
                    v-model="menu_hire"
                    :close-on-content-click="false"
                    activator="parent"
                    :disabled="isDisabled"
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
              <label>소속</label>
              <v-select
                hide-details
                variant="outlined"
                v-model="form.company_affiliation"
                :items="select_items.company_affiliation"
                single-line
                :disabled="isDisabled"
              />
            </div>
            <div class="input_cont mb-3">
              <label>근무부서</label>
              <v-select
                hide-details
                variant="outlined"
                v-model="form.department"
                :items="select_items.departments"
                single-line
                :disabled="isDisabled"
              />
            </div>
          </div>
          <div class="grid-cols-2">
            <div class="input_cont mb-3">
              <label>직급</label>
              <v-select
                hide-details
                variant="outlined"
                v-model="form.position"
                :items="select_items.positions"
                single-line
                :disabled="isDisabled"
              />
            </div>
            <div class="input_cont mb-3">
              <label>근무상태</label>
              <v-select
                hide-details
                variant="outlined"
                v-model="form.employment_status"
                :items="
                  mode === 'register'
                    ? select_items.employment_status
                    : select_items.all_employment_status
                "
                single-line
                :disabled="isDisabled"
                @change="initResignOptions"
              />
            </div>
          </div>
          <template v-if="form?.employment_status === '퇴직'">
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
                    :disabled="isDisabled && member.role < 2"
                    readonly
                  >
                    <v-menu
                      v-model="menu_resign"
                      :close-on-content-click="false"
                      activator="parent"
                      :disabled="isDisabled && member.role < 2"
                    >
                      <v-date-picker
                        hide-header
                        show-adjacent-months
                        v-model="datepicker_resign"
                        @update:modelValue="
                          form.resign_date = formatDate($event)
                        "
                      />
                    </v-menu>
                  </v-text-field>
                </div>
              </client-only>
            </div>

            <div class="input_cont">
              <label>퇴사사유</label>
              <v-textarea
                row-height="25"
                rows="5"
                variant="outlined"
                auto-grow
                :disabled="isDisabled && member.role < 2"
              />
            </div>
          </template>
        </v-form>
      </v-card-text>

      <v-card-actions class="pt-4 pb-3 px-6 border-top-1">
        <v-btn variant="flat" color="black" text width="80" @click="submit">
          {{ modeText }}
        </v-btn>
        <v-btn
          variant="outlined"
          color="gray-black"
          text
          width="80"
          @click="close"
        >
          취소
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
