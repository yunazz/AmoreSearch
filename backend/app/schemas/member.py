from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class MyPageUpdate(BaseModel):
    member_id: int
    phone: str 

class MyPageResponse(BaseModel):
    member_id: int
    phone: str 
    emp_no: str
    role: int
    name:str
    company_affiliation:str
    phone: str
    employment_status: str
    position: str
    department: str
    
    class Config:
        from_attributes = True
    
class MyPasswordUpdate(BaseModel):
    member_id: int
    password: str
    new_password: str
    password_chk: str

class MemberBase(BaseModel):
    name: str
    emp_no: str
    phone: str
    company_affiliation: Optional[str] = None
    position: str
    employment_status: str
    role: int
    birth_date: date
    hire_date: date 
    resign_date: Optional[date] = None
    resign_date: Optional[date] = None
    resign_reason: Optional[str] = None

class MemberUpdate(BaseModel):
    member_id: int
    name: Optional[str] = None
    emp_no: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    company_affiliation: Optional[str] = None
    position: Optional[str] = None
    employment_status: Optional[str] = None
    role: Optional[int] = None
    birth_date: Optional[date] = None
    hire_date: Optional[date] = None
    resign_date: Optional[date] = None
    resign_date: Optional[date] = None
    resign_reason: Optional[str] = None

class MemberCreate(MemberBase):
    pass

class MembersResponse(MemberCreate):
    created_at: datetime

    class Config:
        from_attributes = True

