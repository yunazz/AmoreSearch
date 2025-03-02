export default defineNuxtPlugin((nuxtApp) => {
  const config = useRuntimeConfig().public.SERVER_HOST;

  const api = $fetch.create({
    baseURL: config + "/api",
  });

  return {
    provide: {
      api,
    },
  };
});
