export default defineNuxtRouteMiddleware(async (to, from) => {
  const login_token = useCookie("login_token");
  const member = useMember();

  if (import.meta.server) {
    if (to.path !== "/") {
      if (!login_token.value) return navigateTo("/");
      const { result }: any = await $fetch(
        "http://localhost:8000/api/auth/me",
        {
          headers: { Authorization: `Bearer ${login_token.value}` },
        }
      );
      if (result) {
        member.value = result;
      } else {
        return navigateTo("/");
      }
    }
  }

  if (
    import.meta.client &&
    to.path !== "/" &&
    (member.value.member_id === 0 || !login_token.value)
  ) {
    if (!login_token.value) return navigateTo("/");
  }

  if (to.path === "/") useCookie("login_token").value = null;
});
