import type { UseFetchOptions } from "nuxt/app";
// let request_count = 0;

// export default <T>(url: string, options: UseFetchOptions<T> = {}) => {
//   const login_token = useCookie("login_token");
//   const config = useRuntimeConfig();

//   const defaults: UseFetchOptions<T> = {
//     headers: { Authorization: `Bearer ${login_token.value ?? ""}` },
//     onRequest({ request, options }) {
//       request_count = request_count + 1;
//       if (import.meta.client) {
//         window.document.querySelector("body")?.classList.add("no-event");
//       }
//     },
//     onRequestError({ request, options, error }) {
//       console.log("onRequestError", error);
//     },
//
//     onResponseError({ request, response, options }) {
//       console.log("onResponseError");
//     },
//   };
//   const settings = defu(options, defaults);

//   return useFetch(url, settings);
// };
const login_token = useCookie("login_token");

export function useApi<T>(
  url: string | (() => string),
  options: UseFetchOptions<T> = {
    headers: { Authorization: `Bearer ${login_token.value ?? ""}` },
    onRequest({ request, options }) {
      console.log("체크");
      // options.headers.set("Authorization", `Bearer ${login_token.value ?? ""}`);
    },
    onResponseError({ request, response, options }) {
      console.log("onResponseError");
      navigateTo("/");
    },
  }
) {
  return useFetch(url, {
    ...options,
    $fetch: useNuxtApp().$api as typeof $fetch,
  });
}
