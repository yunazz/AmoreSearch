export const enums = {
  roles: { 0: "", 1: "일반사용자", 2: "관리자", 3: "시스템관리자" },
  brand_ctgry: {
    BEAUTY_CARE: "화장품",
    PERFUME: "향수",
    MEDICAL_BEAUTY: "메디컬뷰티",
    BEAUTY_DEVICE: "디바이스",
    INNER_BEAUTY: "이너뷰티",
    HAIR: "헤어",
    BODY: "바디",
    ORAL_CARE: "덴탈",
    TEA_CULTURE: "티컬처",
  },
};

export const select_items = {
  departments: ["HR팀", "법무팀", "영업팀"],
  company_affiliation: ["아모레퍼시픽그룹", "아모레퍼시픽", "설화수"],
  positions: ["사원", "대리", "팀장", "과장", "차장", "부장", "임원"],
  employment_status: ["재직", "휴직", "정직"],
  all_employment_status: ["재직", "휴직", "정직", "퇴직"],
};

export const ourBrands = [
  { name: "설화수", img_path: "/img/logo/sulwhasoo.png" },
  { name: "라네즈", img_path: "/img/logo/laneige.png" },
  { name: "이니스프리", img_path: "/img/logo/innisfree.png" },
  { name: "에이피뷰티", img_path: "/img/logo/ap.png" },
  { name: "헤라", img_path: "/img/logo/hera.png" },
  { name: "프리메라", img_path: "/img/logo/primera.png" },
  { name: "아이오페", img_path: "/img/logo/iope.png" },
  { name: "마몽드", img_path: "/img/logo/mamonde.png" },
  { name: "한율", img_path: "/img/logo/hanyul.png" },
  { name: "에스트라", img_path: "/img/logo/aestura.png" },
  { name: "에스쁘아", img_path: "/img/logo/espoir.png" },
  { name: "에뛰드", img_path: "/img/logo/house.png" },
  { name: "려", img_path: "/img/logo/ryo.png" },
  { name: "미쟝센", img_path: "/img/logo/mise_en_scene.png" },
  { name: "라보에이치", img_path: "/img/logo/laboh.png" },
  { name: "아윤채", img_path: "/img/logo/ayunche.jpg" },
  { name: "아모스프로페셔널", img_path: "/img/logo/amos_professional.png" },
  { name: "롱테이크", img_path: "/img/logo/longtake.png" },
  { name: "일리윤", img_path: "/img/logo/illiyoon.png" },
  { name: "해피바스", img_path: "/img/logo/happybath.png" },
  { name: "스킨유", img_path: "/img/logo/skin_u.png" },
  { name: "메디안", img_path: "/img/logo/median.png" },
  { name: "젠티스트", img_path: "/img/logo/gentist.png" },
  { name: "구딸", img_path: "/img/logo/paris.png" },
  { name: "바이탈뷰티", img_path: "/img/logo/vitalbeautie.png" },
  { name: "메이크온", img_path: "/img/logo/makeon.png" },
  { name: "오딧세이", img_path: "/img/logo/odyssey.png" },
  { name: "비레디", img_path: "/img/logo/beready.png" },
  { name: "홀리추얼", img_path: "/img/logo/holitual.jpg" },
  { name: "오설록", img_path: "/img/logo/osulloc.png" },
];

export const boardCategory = {
  NEWS: [
    { name: "전체", value: "" },
    { name: "기업", value: "기업" },
    { name: "브랜드", value: "브랜드" },
    { name: "연구개발", value: "연구개발" },
    { name: "사회공헌", value: "사회공헌" },
    { name: "지속가능경영", value: "지속가능경영" },
  ],
  BRAND: [
    { name: "전체", value: "" },
    { name: "화장품", value: "BEAUTY_CARE" },
    { name: "향수", value: "PERFUME" },
    { name: "메디컬뷰티", value: "MEDICAL_BEAUTY" },
    { name: "디바이스", value: "BEAUTY_DEVICE" },
    { name: "이너뷰티", value: "INNER_BEAUTY" },
    { name: "헤어", value: "HAIR" },
    { name: "바디", value: "BODY" },
    { name: "덴탈", value: "ORAL_CARE" },
    { name: "티컬처", value: "TEA_CULTURE" },
  ],
  REPORT: [
    { name: "전체", value: "" },
    { name: "재무제표", value: "재무제표" },
    { name: "실적발표", value: "경영실적" },
    { name: "사업보고서", value: "사업보고서" },
    { name: "영업보고서", value: "영업보고서" },
    { name: "기타IR", value: "기타IR" },
  ],
};

export const externalCategory = {
  NEWS: [{ name: "코스인코리아닷컴", value: "코스인코리아닷컴" }],
  JOURNAL: [
    { name: "코스메틱리포트", value: "코스메틱리포트" },
    { name: "ALLURE", value: "ALLURE" },
  ],
  COSMETIC: [
    { name: "전체", value: "" },
    { name: "스킨", value: "스킨" },
    { name: "메이크업", value: "메이크업" },
    { name: "클렌징", value: "클렌징" },
    { name: "선케어", value: "선케어" },
    { name: "바디", value: "바디" },
    { name: "헤어", value: "헤어" },
  ],
};
