<script setup>
const lnb_items = [
  { name: "AI서치", path: "/home" },
  { name: "아모레스토리", path: "/amorestory" },
  { name: "NEWS", path: "/news" },
  { name: "화장품", path: "/products" },
  { name: "즐겨찾기", path: "/favorites" },
  { name: "사원관리", path: "/members" },
];
const member = ref({
  name: "홍길동",
});
const route = useRoute();

function active_menu(path) {
  console.log(route.path.indexOf(path));
  return route.path.indexOf(path) > -1;
}
</script>
<template>
  <nav id="lnb">
    <div class="lnb_top">
      <h1>AmoreSearch</h1>
      <div class="lnb_myprofile">
        <v-icon class="ma-2" icon="mdi-account-circle" variant="text" />
        <div>
          <p class="fw-500">{{ member.name }}</p>
          <div><span>사원</span> / <span>HR팀</span></div>
        </div>
      </div>
      <div class="lnb_menu">
        <small class="text-gray-04">OVERVIEW</small>
        <ul class="lnb_list">
          <li
            v-for="item in lnb_items"
            :key="item.label"
            :class="{ active: active_menu(item.path) }"
          >
            <a :href="item.path">
              <v-icon class="ma-2" icon="mdi-menu" variant="text" />
              <span>{{ item.name }}</span>
            </a>
          </li>
        </ul>
      </div>
    </div>
    <div class="lnb_bottom">
      <div>
        <v-btn class="ma-2" icon="mdi-logout" variant="text" />
      </div>
    </div>
  </nav>
</template>
<style scoped>
nav#lnb {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  width: 200px;
  padding: 30px 20px 16px;
  background: #fff;
  box-shadow: rgba(17, 17, 26, 0.05) 0px 1px 0px,
    rgba(17, 17, 26, 0.1) 0px 0px 8px;
}
nav#lnb h1 {
  font-size: 20px;
}
.lnb_bottom > div {
  display: flex;
  justify-content: flex-end;
}
.lnb_myprofile {
  display: flex;
  align-items: center;
  column-gap: 0.25rem;
  margin-top: 1.25rem;
  margin-bottom: 1.125rem;
}
.lnb_myprofile div {
  line-height: 1.125rem;
}
.lnb_myprofile div p {
  display: flex;
  column-gap: 2px;
}
.lnb_myprofile div div {
  font-size: 0.75rem;
}
.lnb_list {
  margin-top: 2px;
}
.lnb_list li a {
  display: flex;
  align-items: center;
  text-decoration: none;
  column-gap: 0.25rem;
}
.lnb_list li a i {
  margin-left: 0 !important;
}
</style>
