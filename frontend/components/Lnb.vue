<script setup>
const lnb_items = [
  { name: 'AI서치', path: '/ai_search' },
  { name: '아모레스토리', path: '/amorestory' },
  { name: 'NEWS', path: '/news' },
  { name: '화장품', path: '/products' },
  { name: '즐겨찾기', path: '/favorites' },
];
const admin_items = [{ name: '사원관리', path: '/members' }];
const member = ref({
  name: '홍길동',
  position: '사원',
  department: 'HR',
});
const route = useRoute();

function active_menu(path) {
  console.log(route.path.indexOf(path));
  return route.path.indexOf(path) > -1;
}

function logout() {}
</script>
<template>
  <nav id="lnb">
    <div class="lnb_top">
      <h1 class="buri">AmoreSearch</h1>
      <NuxtLink class="lnb_myprofile" to="/mypage">
        <v-icon class="ma-2" icon="mdi-account-circle" variant="text" />
        <div>
          <div class="text-gray-01 fw-500">
            <span>{{ member.department }}</span>
          </div>
          <p class="fw-800">
            {{ member.name }}
            <span class="fw-500"> {{ member.position }}</span>
          </p>
        </div>
      </NuxtLink>
      <div class="lnb_menu">
        <small class="text-gray-01">OVERVIEW</small>
        <ul class="lnb_list">
          <li
            v-for="item in lnb_items"
            :key="item.label"
            :class="{ active: active_menu(item.path) }"
          >
            <NuxtLink :to="item.path">
              <v-icon class="ma-2" icon="mdi-menu" variant="text" />
              <span>{{ item.name }}</span>
            </NuxtLink>
          </li>
        </ul>
        <small class="text-gray-01">ADMIN</small>
        <ul class="lnb_list">
          <li
            v-for="item in admin_items"
            :key="item.label"
            :class="{ active: active_menu(item.path) }"
          >
            <NuxtLink :to="item.path">
              <v-icon class="ma-2" icon="mdi-menu" variant="text" />
              <span>{{ item.name }}</span>
            </NuxtLink>
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
  width: var(--lnb-width);
  min-width: var(--lnb-width);
  background: var(--lnb-bg-color);
  color: white;
  box-shadow: rgba(17, 17, 26, 0.05) 0px 1px 0px,
    rgba(17, 17, 26, 0.1) 0px 0px 8px;
}
nav#lnb h1 {
  font-size: 24px;
  padding: 36px 20px 0 20px;
}
.lnb_bottom > div {
  display: flex;
  justify-content: flex-end;
}
.lnb_myprofile {
  display: flex;
  align-items: center;
  column-gap: 0.25rem;
  margin-top: 1.5rem;
  margin-bottom: 0.75rem;
  padding: 0 12px;
  padding-bottom: 6px;
  text-decoration: none;
  color: white;
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
.lnb_menu {
  border-top: 1px solid #454545;
}
.lnb_menu small {
  display: block;
  margin-top: 16px;
  padding: 0 20px;
}
.lnb_list {
  padding: 0 8px;
  margin-top: 4px;
}
.lnb_list li {
  margin: 2px 0;
}
.lnb_list li a {
  display: flex;
  align-items: center;
  text-decoration: none;
  column-gap: 0.25rem;
  padding: 0 16px;
  color: white;
}
.lnb_list li a i {
  margin-left: 0 !important;
}
.lnb_list li.active {
  /* background: #f5f5f5; */
  background: #454545;
  border-radius: 20px;
}
.lnb_list li.active a {
  font-weight: 600;
  /* color: var(--main-color); */
  color: white;
}
</style>
