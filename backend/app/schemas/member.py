from pydantic import BaseModel
from typing import Optional
from datetime import date

class MyPageUpdate(BaseModel):
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
    password: str
    new_password: str

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
    resign_reason: Optional[str] = None