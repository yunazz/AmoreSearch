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

      // const { result, code }: any = await $fetch('/api/member/me', {
      // 	headers: { Authorization: `Bearer ${str_login_token}` }
      // });
      // if (code === 0) member.value = result;
      // refreshCookie('login_token');
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
    // name: '',
    // position: '',
    // department: '',
    // role: ''
    role: 2,
    name: "홍길동",
    company_affiliation: "",
    birth_date: "",
    phone: "",
    hire_date: "",
    employment_status: "재직",
    position: "사원",
    department: "HR팀",
  });
  return member;
}
