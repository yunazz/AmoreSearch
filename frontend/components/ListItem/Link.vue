<script setup>
const props = defineProps(["item"]);
// const emit = defineEmits(["close"]);
function linkFnc(url) {
  window.open(url);
}
function downloadFnc(item) {
  window.open(item.original_file_url);
}
function addFavorites(item) {
  console.log(item);
}
</script>

<template>
  <div external class="list-item">
    <div class="list-left">
      <p class="list-title">{{ item.title }}</p>
      <p class="list-text text-clamp-2">{{ item.content }}</p>
      <p>
        <span class="text-gray-04 mr-2">{{
          formatDate(item.published_at || item.created_at)
        }}</span>
        <span class="text-gray-04" v-if="item.source_name">
          {{ item.source_name }}
        </span>
      </p>
    </div>
    <div>
      <template v-if="item?.original_file_url">
        <v-btn
          color="grey-lighten-2"
          icon="mdi-folder"
          variant="text"
          @click="downloadFnc(item)"
        />
      </template>
      <template v-else>
        <v-btn
          color="grey-lighten-1"
          icon="mdi-link"
          variant="text"
          @click="linkFnc(item.source_url)"
        />
      </template>

      <v-btn
        class="icon--toggle"
        icon="mdi-star"
        variant="text"
        @click="addFavorites(item)"
      />
    </div>
  </div>
</template>

<style scoped>
.list-item {
  padding: 10px 16px;
  text-decoration: none;
}
.list-item {
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: center;
  border-top: 1px solid var(--border-color);
}
.list-item .list-title {
  font-weight: 500;
  line-height: 1.5rem;
  font-size: 0.9375rem;
  margin-bottom: 2px;
}
.list-left {
  width: calc(100% - 120px);
}
.list-item p {
  font-size: 0.8125rem;
  line-height: 1rem;
}
.list-item p.list-text {
  margin-bottom: 4px;
  font-size: 0.8125rem;
}

.list-item:last-of-type {
  border-bottom: 1px solid var(--border-color);
}
</style>
