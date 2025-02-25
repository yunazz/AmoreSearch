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
    emp_no: "2045910583",
    role: 2,
    name: "홍길동",
    company_affiliation: "아모레퍼시픽",
    birth_date: "1995-01-01",
    phone: "010-4470-1111",
    hire_date: "2020-01-01",
    employment_status: "재직",
    position: "사원",
    department: "HR팀",
  });
  return member;
}
