import type { UseFetchOptions } from "nuxt/app";

export function useApi<T>(
  url: string | (() => string),
  options: UseFetchOptions<T> = {
    onRequest({ request, options }) {
      const login_token = useCookie("login_token");
      console.log("체크");
      options.headers.set("Authorization", `Bearer ${login_token.value ?? ""}`);
    },
    onResponseError({ request, response, options }) {
      console.log("onResponseError");
    },
  }
) {
  return useLazyFetch(url, {
    ...options,
    $fetch: useNuxtApp().$api as typeof $fetch,
  });
}
