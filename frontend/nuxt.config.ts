// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  server: {
    host: "0.0.0.0",  // 외부 접속 허용
    port: 3000
  },
})
