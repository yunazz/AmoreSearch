from fastapi import APIRouter, Depends, Query, HTTPException
from typing import Optional
from sqlalchemy.orm import Session
from db.session import get_session 
from db.connection import get_connection 
from schemas.response import BaseResponse
from schemas.member import MyPageUpdate, MyPageResponse, MyPasswordUpdate, MemberBase, MemberCreate, MemberUpdate, MembersResponse
from core.security import create_access_token, hash_password, decode_access_token, verify_password
from model import Member 
from fastapi.security import  OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


router = APIRouter()

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


# ✅ 즐겨찾기 조회
@router.get("/favorites")
def get_favorites(
    favorite_type: str = Query(None),
    query: Optional[str] = Query(None),
    current_page: int = Query(1), 
    item_per_page: int = Query(12),
    token: str= Depends(oauth2_scheme),
):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            member = decode_access_token(token)
            
            sql = f"""
            SELECT * from favorites WHERE member_id = {member.member_id} 
            JOIN document on document.document_id = favorite.document_id 
            JOIN document on document.document_id = favorite.document_id 
            """
            count_sql = f"SELECT COUNT(*) from favorites WHERE member_id = {member.member_id}"
            params = []

            if favorite_type:
                sql += " AND favorite_type = %s"
                count_sql += " AND favorite_type = %s"
                params.append(favorite_type)

            if query:
                sql += " AND (title LIKE %s OR content LIKE %s)"
                count_sql += " AND (title LIKE %s OR content LIKE %s)"
                params.extend([f"%{query}%", f"%{query}%"])
            
            # 총 개수 조회
            cursor.execute(count_sql, params) 
            total_count = cursor.fetchone()["COUNT(*)"]

            # ORDER BY
            sql += " ORDER BY created_at DESC"
            
            # 페이징 적용
            offset = (current_page - 1) * item_per_page
            sql += " LIMIT %s OFFSET %s"
            params.extend([item_per_page, offset])

            # 데이터 조회
            cursor.execute(sql, params)
            result = cursor.fetchall()

            return BaseResponse(
                code=0,
                msg="조회 성공",
                result=result,
                paging={
                    "total_rows": total_count,
                    "current_page": current_page,
                }
            )

    finally:
        conn.close()

    return BaseResponse(code=1, msg="조회 실패")


# ✅ 즐겨찾기 추가
@router.post("/favorites")
def add_favorites(
    scope: str, 
    target_id: int, 
    favorite_type: str,
    token: str= Depends(oauth2_scheme),
):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            member = decode_access_token(token)
            
            cursor.execute(
                'INSERT INTO favorites (scope, favorite_type, target_id, member_id) values (%s, %s, %s)', 
                [scope, favorite_type, target_id, target_id, member.member_id]
            )
    finally:
        conn.close()
        
        
# ✅ 즐겨찾기 삭제
@router.put("/favorites")
def remove_favorites():
    pass