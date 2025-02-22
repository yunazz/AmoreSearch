type RoleTypes = 3 | 2 | 1 | 0; // '시스템관리자' | '관리자' | '일반' | '';

interface ResponseOutput {
  code: number;
  msg: String;
  result: any;
  total_rows?: any;
}

interface JwtPayloadOptions {
  member_id: number;
  emp_no: string;
  position: string;
  department: string;
  name: string;
  role: RoleTypes;
}

export interface MemberOptions extends JwtPayloadOptions {}
