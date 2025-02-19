import { createVuetify } from 'vuetify';
import { aliases, mdi } from 'vuetify/iconsets/mdi'
import * as components from 'vuetify/components'
import 'vuetify/styles';

export default defineNuxtPlugin((app) => {
  const vuetify = createVuetify({
    icons: {
      defaultSet: 'mdi',
      aliases,
      sets: {
        mdi,
      },
    },
    components,
    theme: {
      themes: {
        light: {
          dark: false,
          colors: {
            main: '#000000',
            // main: '#954DD1',
            // sub_1: '#12043e',
            // sub_2: '#12043e',
            // sub_3: '#5215fc',
            // sub_4: '#885fff',
            // sub_5: '#d3d2f1',
          },
        },
      },
    },
  
  });
  app.vueApp.use(vuetify);
});
