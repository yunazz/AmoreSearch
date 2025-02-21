<script setup>
const tab = ref("MEMBER");
const tabItems = ref([
  { text: "현직직원", value: "MEMBER" },
  { text: "퇴사직직원", value: "NO_MEMBER" },
]);
const list1 = ref([
  {
    member_id: 1,
    role: "일반",
    emp_no: "1032645132",
    name: "홍길동",
    company_affiliation: "아모레퍼시픽",
    department: "HR팀",
    position: "사원",
    birth_date: "1995-01-01",
    phone: "01044701123",
    hire_date: "2010-01-01",
    work_status: "재직",
  },
  {
    member_id: 2,
    role: "일반",
    emp_no: "1032645133",
    name: "김영희",
    company_affiliation: "아모레퍼시픽그룹",
    department: "재무팀",
    position: "대리",
    birth_date: "1990-05-12",
    phone: "01051237894",
    hire_date: "2012-06-15",
    work_status: "재직",
  },
  {
    member_id: 3,
    role: "일반",
    emp_no: "1032645134",
    name: "박철수",
    company_affiliation: "설화수",
    department: "마케팅팀",
    position: "과장",
    birth_date: "1987-09-23",
    phone: "01092345678",
    hire_date: "2008-09-01",
    work_status: "재직",
  },
  {
    member_id: 4,
    role: "일반",
    emp_no: "1032645135",
    name: "이민호",
    company_affiliation: "에뛰드",
    department: "영업팀",
    position: "대리",
    birth_date: "1992-11-05",
    phone: "01011055678",
    hire_date: "2015-03-10",
    work_status: "재직",
  },
  {
    member_id: 5,
    role: "일반",
    emp_no: "1032645136",
    name: "정수진",
    company_affiliation: "아모레퍼시픽",
    department: "영업팀",
    position: "사원",
    birth_date: "1996-04-18",
    phone: "01098765432",
    hire_date: "2020-07-01",
    work_status: "재직",
  },
  {
    member_id: 6,
    role: "일반",
    emp_no: "1032645137",
    name: "최재혁",
    company_affiliation: "아모레퍼시픽그룹",
    department: "IT팀",
    position: "차장",
    birth_date: "1985-02-27",
    phone: "01033445566",
    hire_date: "2007-12-20",
    work_status: "재직",
  },
  {
    member_id: 7,
    role: "일반",
    emp_no: "1032645138",
    name: "김서연",
    company_affiliation: "이니스프리",
    department: "마케팅팀",
    position: "대리",
    birth_date: "1991-07-09",
    phone: "01077889900",
    hire_date: "2013-08-05",
    work_status: "재직",
  },
  {
    member_id: 8,
    role: "일반",
    emp_no: "1032645139",
    name: "오지훈",
    company_affiliation: "아모레퍼시픽",
    department: "연구원",
    position: "과장",
    birth_date: "1988-06-14",
    phone: "01022334455",
    hire_date: "2009-11-25",
    work_status: "재직",
  },
  {
    member_id: 9,
    role: "일반",
    emp_no: "1032645140",
    name: "한예린",
    company_affiliation: "에뛰드",
    department: "영업팀",
    position: "사원",
    birth_date: "1997-08-30",
    phone: "01011223344",
    hire_date: "2021-05-17",
    work_status: "재직",
  },
  {
    member_id: 10,
    role: "일반",
    emp_no: "1032645141",
    name: "유준석",
    company_affiliation: "아모레퍼시픽그룹",
    department: "법무팀",
    position: "부장",
    birth_date: "1982-12-03",
    phone: "01044556677",
    hire_date: "2005-01-10",
    work_status: "재직",
  },
]);

const totals = list1.value.length;
const propItem = ref(null);
const dialog = ref({
  edit: false,
  register: false,
});

function openDialog(dialogName, item) {
  dialog.value[dialogName] = true;
  propItem.value = item;
}

function closeDialog(mode) {
  dialog.value[dialogName] = false;
  propItem.value = null;
}

async function submitDialog(mode, formData) {
  if (mode === "edit") {
    await editMember();
    // 간단 리프레쉬만
  } else if (mode === "register") {
    await registerMember();
    // 페이지 1로 돌리기기
  }
  console.log(mode);
  closeDialog(mode);
}

async function editMember() {}
async function registerMember() {}
</script>
<template>
  <div id="Members" class="content">
    <div class="content_inner">
      <div class="page_header">
        <h2 class="page_title">직원관리</h2>
        <v-tabs
          class="tab_narrow"
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
      </div>
      <div class="board">
        <div class="board_util">
          <v-btn icon="mdi-plus" />
        </div>
        <div class="board_list">
          <template v-if="tab === 'MEMBER'">
            <v-table>
              <thead>
                <tr>
                  <th class="text-center" style="width: 80px">번호</th>
                  <th class="text-left">권한</th>
                  <th class="text-left">사번</th>
                  <th class="text-left">이름</th>
                  <th class="text-left">소속</th>
                  <th class="text-left">부서</th>
                  <th class="text-left">직급</th>
                  <th class="text-left" style="width: 120px">생년월일</th>
                  <th class="text-left" style="width: 140px">휴대폰번호</th>
                  <th class="text-left" style="width: 120px">입사일</th>
                  <th class="text-left" style="width: 90px">근무상태</th>
                  <th class="text-left" style="width: 80px">수정</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item, index) in list1" :key="item.name">
                  <td class="text-center">{{ totals - index }}</td>
                  <td>{{ item.role }}</td>
                  <td>{{ item.emp_no }}</td>
                  <td>{{ item.name }}</td>
                  <td>{{ item.company_affiliation }}</td>
                  <td>{{ item.department }}</td>
                  <td>{{ item.position }}</td>
                  <td>{{ item.birth_date }}</td>
                  <td>{{ item.phone }}</td>
                  <td>{{ item.hire_date }}</td>
                  <td>{{ item.work_status }}</td>
                  <td>
                    <v-btn
                      :id="`member-${index}`"
                      icon="mdi-pencil"
                      @click="openDialog('edit', item)"
                      variant="text"
                    />
                  </td>
                </tr>
              </tbody>
            </v-table>
          </template>
        </div>

        <div class="board_paging">1,2,3,</div>
      </div>
    </div>
    <v-dialog v-model="dialog.edit" max-width="600">
      <FormMember
        mode="edit"
        item="propItem"
        @close="closeDialog"
        @submit="submitDialog"
      />
    </v-dialog>
    <v-dialog v-model="dialog.register" max-width="600">
      <FormMember mode="register" @close="closeDialog" @submit="submitDialog" />
    </v-dialog>
  </div>
</template>

<style scoped></style>
