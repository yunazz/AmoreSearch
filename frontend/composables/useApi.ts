import type { UseFetchOptions } from "nuxt/app";
const login_token = useCookie("login_token");

export function useApi<T>(
  url: string | (() => string),
  options: UseFetchOptions<T> = {
    headers: { Authorization: `Bearer ${login_token.value ?? ""}` },
    server: false,
    onRequest({ request, options }) {
      console.log("체크");
      // options.headers.set("Authorization", `Bearer ${login_token.value ?? ""}`);
    },
    onResponseError({ request, response, options }) {
      console.log("onResponseError");
    },
  }
) {
  return useFetch(url, {
    ...options,
    $fetch: useNuxtApp().$api as typeof $fetch,
  });
}
