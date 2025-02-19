import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  server: {
    host: "0.0.0.0", 
    port: 3000
  },
  css: ['~/assets/css/font.css','~/assets/css/common.css','~/assets/css/main.css', '~/assets/css/vuetify.css'],
  build: {
    transpile: ['vuetify'],
  },
  modules: [
    (_options, nuxt) => {
      nuxt.hooks.hook('vite:extendConfig', (config) => {
        config.plugins.push(vuetify({ autoImport: true }))
      })
    },
    '@nuxt/image'
  ],
  vite: {
    vue: {
      template: {
        transformAssetUrls,
      },
    },
  },
  head: {
    link: [
      {
        rel: 'stylesheet',
        href: 'https://fonts.googleapis.com/css?family=Material+Icons|Material+Icons+Round'
      }
    ]
  }
})
