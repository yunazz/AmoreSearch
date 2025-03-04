from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from sqlalchemy.orm import Session
from schemas.response import BaseResponse
from models.member import Member 
from fastapi.security import  OAuth2PasswordBearer
from schemas.member import MyPageUpdate, MyPageResponse, MyPasswordUpdate, MemberBase, MemberCreate, MemberUpdate, MembersResponse
from db.session import get_session 
from core.security import create_access_token, hash_password, decode_access_token, verify_password

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# ✅ 내 정보 수정
@router.put("/me")
def update_me(form_data: MyPageUpdate, token: str= Depends(oauth2_scheme), db: Session = Depends(get_session)):
    member = decode_access_token(token)
    
    db_member = db.query(Member).filter(Member.member_id == member.get('member_id')).first()

    if not db_member:
        raise HTTPException(status_code=200, detail={"code":1, "msg":"로그인 정보 수정 오류"})

    db_member.phone = form_data.phone
    db.commit()
    db.refresh(db_member) 
    
    
    me_data = MyPageResponse.model_validate(db_member, from_attributes=True)

    access_token = create_access_token(data=me_data.model_dump())

    return BaseResponse(msg="수정되었습니다.", code=0, result=access_token)

# ✅ 내 비밀번호 수정
@router.put("/password")
def update_my_password(form_data: MyPasswordUpdate, token: str= Depends(oauth2_scheme), db: Session = Depends(get_session)):
    member = decode_access_token(token)
    
    db_member = db.query(Member).filter(Member.member_id == member.get('member_id')).first()
    
    if not verify_password(form_data.password, db_member.password):
        return BaseResponse(code=1, msg="현재 비밀번호가 일치하지 않습니다.")

    new_password = hash_password(form_data.new_password)
    db_member.password = new_password
    db.commit()
    db.refresh(db_member) 
    return BaseResponse(code=0, msg="변경되었습니다.",)

# # ✅ 회원 생성
# @router.post("/", response_model=MembersResponse)
# def add_member(member: MemberCreate, db: Session = Depends(get_session)):
#     db_member = add_member(db=db, member=member)
#     if not db_member:
#         raise HTTPException(status_code=400, detail="회원 생성 실패")
#     return db_member

# # ✅ 회원 조회 (단일)
# @router.get("/{member_id}", response_model=MembersResponse)
# def get_member(member_id: int, db: Session = Depends(get_session)):
#     db_member = get_member(db=db, member_id=member_id)
#     if db_member is None:
#         raise HTTPException(status_code=404, detail="회원이 존재하지 않습니다.")
#     return db_member

# # ✅ 모든 회원 조회 (페이징 처리)
# @router.get("/members/", response_model=list[MembersResponse])
# def get_members(skip: int = 0, limit: int = 10, db: Session = Depends(get_session)):
#     members = get_members(db=db, skip=skip, limit=limit)
#     return members

