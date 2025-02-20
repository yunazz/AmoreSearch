<script setup>
// const router = useRouter();
const member = ref({
  name: "홍길동",
  position: "사원",
  department: "HR",
});
const formData = ref({});
</script>

<template>
  <div id="AiSearch" class="page">
    <div class="contents">
      <h2 class="title--xl fw-700">
        안녕하세요,
        <span class="text-underline ml-1">
          {{ member.name }} {{ member.position }}님
        </span>
        <br />
        무엇을 도와드릴까요?
      </h2>
      <div class="input--search mt-5">
        <v-icon icon="mdi-magnify" />
        <input type="text" />
      </div>
    </div>
    <v-divider class="mt-9" />
    <article class="mt-7">
      <v-sheet class="group_card" style="">
        <v-slide-group v-model="model" class="pa-2" show-arrows>
          <v-slide-group-item v-for="n in 8" :key="n">
            <div class="group_card_item">
              <!-- <v-card :class="['ma-4']" height="250" width="340" @click="toggle"> -->
              <div class="d-flex fill-height align-center justify-center">
                item
              </div>
              <!-- </v-card> -->
            </div>
          </v-slide-group-item>
        </v-slide-group>
      </v-sheet>
    </article>
    <div class="container_inner grid-cols-2">
      <article class="mt-2 px-3">
        <v-card class="mx-auto" elevation="0">
          <v-list :items="items" lines="two" item-props>
            <template v-slot:prepend>
              <v-avatar color="grey-lighten-1">
                <NuxtImg src="img/icon/story.svg" width="30" />
              </v-avatar>
            </template>
            <template v-slot:subtitle="{ subtitle }">
              <div v-html="subtitle"></div>
            </template>
            <template v-slot:append>
              <v-btn
                color="grey-lighten-2"
                icon="mdi-star"
                variant="text"
              ></v-btn>
            </template>
          </v-list>
        </v-card>
      </article>
      <article class="mt-2 px-3">
        <v-card class="mx-auto" elevation="0">
          <v-list :items="items1" lines="two" item-props>
            <template v-slot:prepend>
              <v-avatar color="grey-lighten-1">
                <v-icon color="white">mdi-folder</v-icon>
              </v-avatar>
            </template>
            <template v-slot:subtitle="{ subtitle }">
              <div v-html="subtitle"></div>
            </template>
          </v-list>
        </v-card>
      </article>
    </div>
  </div>
</template>

<style scoped>
.v-field.v-field--prepended {
  border-radius: 34px;
}

#AiSearch h2 {
  /* text-align: center; */
  font-size: 1.75rem;
  line-height: 2.5rem;
  word-spacing: -4px;
}
.text-underline {
  font-weight: 800;
  text-underline-offset: 7px;
}
.input--search {
  margin-top: 2px;
  /* max-width: 800px; */
  /* margin: 0 auto; */
  /* margin-top: 0.75rem; */
}
</style>
