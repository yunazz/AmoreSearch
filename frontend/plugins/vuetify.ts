import '@mdi/font/css/materialdesignicons.css';

import 'vuetify/styles';
import { createVuetify } from 'vuetify';

export default defineNuxtPlugin((app) => {
  const vuetify = createVuetify({
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
    components: {
    },
  });
  app.vueApp.use(vuetify);
});
