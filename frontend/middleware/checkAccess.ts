export default defineNuxtRouteMiddleware(async (to, from) => {
  const nuxtApp = useNuxtApp();
  const login_token = useCookie("login_token");

  let member = useMember().value;

  try {
    if (process.server) {
      const { result }: any = await $fetch("/api/member/me", {
        headers: { Authorization: `Bearer ${login_token.value}` },
      });
      if (result) member = result;
    }
  } catch (e) {
    console.log(e);
  }

  if (!is_empty(member) && member.role !== 0) {
    return nuxtApp.runWithContext(() => navigateTo("/tourney"));
  }
});
