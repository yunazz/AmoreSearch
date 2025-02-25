import { createVuetify } from "vuetify";
import * as components from "vuetify/components";
import "@mdi/font/css/materialdesignicons.css";
import "vuetify/styles";

export default defineNuxtPlugin((app) => {
  const vuetify = createVuetify({
    components,
    icons: {
      defaultSet: "mdi",
    },
    theme: {
      themes: {
        light: {
          dark: false,
          colors: {
            primary: "#784aab",
            main: "#784AAB",
            sub: "#A28DD4",
            black: "#10021a",
            borderColor: "#10021a",
            "on-background": "#10021a",
            "on-surface": "#10021a",
            "on-surface-bright": "#10021a",
            "on-surface-light": "#10021a",
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
