<script setup>
definePageMeta({
  middleware: ["auth"],
});

const member = useMember();
const tabs = ref([
  { text: "재직직원", value: "" },
  { text: "퇴직직원", value: "퇴직" },
]);
const employment_status = ref({ text: "재직직원", value: "MEMBER" });

const filter = ref({
  employment_status: "",
  query: "",
  current_page: 1,
  item_per_page: 20,
});

const filter_query = computed(() => ({
  employment_status: filter.value.employment_status,
  current_page: filter.value.current_page,
  item_per_page: filter.value.item_per_page,
}));

function changePage(current_page) {
  if (current_page === filter.value.current_page) {
    return;
  }
  filter.value.current_page = current_page;
  scrollToTop();
}
const { data: board, status } = useApi("/member/list", {
  key: "member-list",
  query: filter_query,
});

const total_cnt = computed(() => board.value.paging.total_rows);

const propItem = ref(null);

const dialog = ref(false);
const dialogMode = ref(null);

function openDialog(mode, item) {
  dialogMode.value = mode;
  propItem.value = item;
  dialog.value = true;
}

function closeDialog(mode) {
  dialog.value = false;
  dialogMode.value = null;
}

async function submitDialog(mode, formData) {
  if (mode === "edit") {
    await editMember();
    // 간단 리프레쉬만
  } else if (mode === "register") {
    await registerMember();
    // 페이지 1로 돌리기기
  }
  closeDialog(mode);
}

async function editMember() {}
async function registerMember() {}

watch(employment_status, (newValue) => {
  filter.value.employment_status = newValue.value;
  filter.value.current_page = 1;
});
</script>

<template>
  <div id="Members" class="content">
    <div class="content_inner">
      <div class="page_header">
        <h2 class="page_title">직원관리</h2>
        <div class="board_tab depth-1">
          <ClientOnly>
            <v-tabs
              v-model="employment_status"
              bg-color="transparent"
              align-tabs="center"
              density="comfortable"
              selected-class="text-primary"
            >
              <v-tab
                v-for="tab in tabs"
                :key="tab.value"
                :text="tab.text"
                :value="tab"
                :ripple="false"
              />
            </v-tabs>
          </ClientOnly>
        </div>
      </div>
      <div class="board">
        <div class="board_util">
          <div class="board_desc">
            <span class="body--m text-gray-03">total: {{ total_cnt }}</span>
          </div>
          <small v-if="employment_status.value === 'NO_MEMBER'" class="ml-2">
            퇴직직원의 정보는 관리자만 수정 가능합니다.
          </small>
          <v-btn
            v-if="employment_status.value === 'MEMBER'"
            density="comfortable"
            icon="mdi-plus"
            color="black"
            @click="openDialog('register')"
          />
        </div>

        <div class="board_list">
          <v-table>
            <thead>
              <tr>
                <th class="text-center" style="width: 78px">번호</th>
                <th>이름</th>
                <th>사번</th>
                <th>소속</th>
                <th>부서</th>
                <th>직급</th>
                <th style="width: 120px">생년월일</th>
                <th style="width: 140px">휴대폰번호</th>
                <th style="width: 120px">입사일</th>
                <th style="width: 90px">근무상태</th>
                <th class="text-center" style="width: 70px">수정</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(item, index) in board?.result" :key="item.name">
                <!-- @click="openDialog('info', item)"
              class="cur-p" -->
                <td class="text-center">{{ total_cnt - index }}</td>
                <td>
                  <v-icon
                    v-if="item.role == 2"
                    icon="mdi-shield-account"
                    color="primary"
                  />
                  {{ item.name }}
                </td>
                <td>{{ item.emp_no }}</td>
                <td>{{ item.company_affiliation }}</td>
                <td>{{ item.department }}</td>
                <td>{{ item.position }}</td>
                <td>{{ item.birth_date }}</td>
                <td>{{ item.phone }}</td>
                <td>{{ item.hire_date }}</td>
                <td>{{ item.employment_status }}</td>
                <td class="text-center">
                  <v-btn
                    :id="`member-${index}`"
                    icon="mdi-account-edit"
                    color="grey-lighten-2"
                    class="icon--toggle"
                    :class="
                      tab === 'MEMBER' || member.role >= 2 ? 'active' : ''
                    "
                    @click.stop="openDialog('edit', item)"
                    variant="text"
                  />
                </td>
              </tr>
            </tbody>
          </v-table>
        </div>

        <Paging
          :paging="filter"
          :status="status"
          :total_row="total_cnt"
          @changePage="changePage"
        />
      </div>
    </div>
    <PopupMember
      v-model="dialog"
      :mode="dialogMode"
      :item="propItem"
      @close="closeDialog"
      @submit="submitDialog"
    />
  </div>
</template>

<style scoped></style>
