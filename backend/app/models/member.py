from sqlalchemy import create_engine, Column, Integer, String, Date, DateTime, TIMESTAMP
from sqlalchemy.orm import declarative_base, mapped_column
from sqlalchemy import UniqueConstraint
from datetime import date, datetime

Base = declarative_base()

class Member(Base):
    __tablename__ = 'member'

    member_id = mapped_column(Integer, primary_key=True, autoincrement=True, comment='회원 고유 ID')
    emp_no = mapped_column(String(10), nullable=False, unique=True, comment='사원번호')
    password = mapped_column(String(100), nullable=False, comment='비밀번호')
    name = mapped_column(String(20), nullable=False, comment='직원이름')
    role = mapped_column(Integer, nullable=False, comment='시스템관리자-3, 관리자-2, 일반-1')
    phone = mapped_column(String(11), nullable=False, comment='휴대폰번호')
    employment_status = mapped_column(String(2), nullable=False, default='재직', comment='재직, 휴직, 정직, 퇴직')
    company_affiliation = mapped_column(String(10), nullable=True, comment='회사 소속')
    position = mapped_column(String(3), nullable=True, comment='회장, 사장, 임원, 과장, 팀장, 대리, 사원')
    department = mapped_column(String(20), nullable=True, comment='부서')
    birth_date = mapped_column(Date, nullable=True, comment='생년월일')
    hire_date = mapped_column(Date, nullable=True, default="CURRENT_TIMESTAMP", comment='입사일')
    resign_date = mapped_column(Date, nullable=True, comment='퇴사일')
    resign_reason = mapped_column(String(100), nullable=True, comment='퇴사 사유')
    created_at = mapped_column(TIMESTAMP, nullable=False, default="CURRENT_TIMESTAMP", comment='등록일시')

    __table_args__ = (
        UniqueConstraint('emp_no', name='emp_no'),
    )