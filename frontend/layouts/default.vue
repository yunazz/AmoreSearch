<script setup></script>
<template>
  <div class="wrap">
    <Lnb />
    <main class="main">
      <slot></slot>
    </main>
  </div>
</template>

<style>
.wrap {
  display: flex;
  background-color: #f5f5f5;
}
main.main {
  height: 100vh;
  background: #fff;
}
</style>
