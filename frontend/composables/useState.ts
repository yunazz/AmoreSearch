import { type MemberOptions } from "~/utils/types";

export const useMember = () =>
  useState<MemberOptions>("member", () => defaultMember().value);

export function useLoginHandler() {
  const member = useMember();
  const login_token = useCookie("login_token", { maxAge: 60 * 60 * 24 * 7 });

  return {
    async refresh(str_login_token?: string) {
      if (str_login_token) {
        login_token.value = str_login_token;
      } else if (login_token.value) {
        str_login_token = login_token.value;
      } else {
        str_login_token = "";
      }

      const response: any = await $fetch("http://localhost:8000/api/auth/me", {
        headers: { Authorization: `Bearer ${str_login_token}` },
      });
      if (response.detail === "성공") member.value = response.result;
      refreshCookie("login_token");
      console.log(member.value);
    },

    logout() {
      login_token.value = null;
      member.value = defaultMember().value;
      refreshCookie("login_token");
    },
  };
}

function defaultMember(): Ref<MemberOptions> {
  const member = ref<MemberOptions>({
    member_id: 0,
    emp_no: "",
    role: 0,
    name: "",
    company_affiliation: "",
    birth_date: "",
    phone: "",
    hire_date: "",
    employment_status: "",
    position: "",
    department: "",
  });
  return member;
}
