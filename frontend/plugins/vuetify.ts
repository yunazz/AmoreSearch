import '@mdi/font/css/materialdesignicons.css'

import 'vuetify/styles'
import { createVuetify } from 'vuetify'

export default defineNuxtPlugin((app) => {
  const vuetify = createVuetify({
    theme: {
      themes: {
        light: {
          dark: false,
          colors: {
            main: '#954DD1', 
            sub_1: '#7C11B2',
            sub_2: '#634ACF',
            sub_3: '#5215FC',
            sub_4: '#885FFF',
            sub_5: '#D3D2F1',
          }
        },
      },
    },
  })
  app.vueApp.use(vuetify)
})
