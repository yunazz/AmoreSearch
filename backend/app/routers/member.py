from fastapi import APIRouter, Depends, Query, HTTPException
from typing import Optional
from sqlalchemy.orm import Session
from db.session import get_session 
from db.connection import get_connection 
from schemas.response import BaseResponse, ListResponse
from schemas.member import MyPageUpdate, MyPageResponse, MyPasswordUpdate, FavoriteRequest
from core.security import create_access_token, hash_password, decode_access_token, verify_password
from model import Member 
from fastapi.security import  OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


router = APIRouter()

# 내 정보 수정
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

# 내 비밀번호 수정
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
    return BaseResponse(code=0, msg="변경되었습니다.")


# 즐겨찾기 조회
@router.get("/favorites")
def get_favorites(
    favorite_type: str = Query(None),
    query: Optional[str] = Query(None),
    current_page: int = Query(1), 
    item_per_page: int = Query(12),
    token: str= Depends(oauth2_scheme),
):
    member = decode_access_token(token)
    
    try:
        conn = get_connection() 
        with conn.cursor() as cursor:
            sql = ""
            count_sql = "SELECT COUNT(*) from favorites"
            params = []

            # favorite_type : 외부뉴스/저널 
            if favorite_type =='EXTERNAL_POST':
                sql +=  """
                SELECT * FROM favorites
                    JOIN post_external ON favorites.target_id = post_external.post_external_id
                    JOIN 
                        (SELECT post_id, image_url from post_image WHERE scope='EXTERNAL' AND image_type='THUMBNAIL') post_image 
                    ON post_external.post_external_id = post_image.post_id
                WHERE favorites.scope='EXTERNAL' AND (favorite_type = 'NEWS' OR favorite_type = 'JOURNAL')
                """
                count_sql += " WHERE scope='EXTERNAL' AND (favorite_type = 'NEWS' OR favorite_type = 'JOURNAL') "
                
            # favorite_type : 회사뉴스
            elif favorite_type =='INTERNAL_NEWS':
                sql +=  """
                SELECT * FROM favorites
                    JOIN post ON target_id = post_id
                    JOIN 
                        (SELECT post_id, image_url from post_image WHERE scope='INTERNAL' AND image_type='THUMBNAIL') post_image 
                    ON post.post_id = post_image.post_id
                WHERE favorites.scope='INTERNAL' AND favorite_type = 'NEWS'
                """
                count_sql += " WHERE scope='INTERNAL' AND favorite_type = 'NEWS'"
                
            # favorite_type : 화장품
            elif favorite_type =='COSMETIC':
                sql +=  """
                SELECT *,
                    CASE
                        WHEN favorites.scope = 'EXTERNAL' THEN cosmetic_external.image_url
                        WHEN favorites.scope = 'INTERNAL' THEN cosmetic.image_url
                        END AS image_url
                FROM favorites
                        LEFT JOIN cosmetic_external ON favorites.scope = 'EXTERNAL' AND favorites.favorite_type = 'COSMETIC' AND favorites.target_id = cosmetic_external.cosmetic_id
                        LEFT JOIN cosmetic ON favorites.scope = 'INTERNAL' AND favorites.favorite_type = 'COSMETIC' AND favorites.target_id = cosmetic.cosmetic_id
                WHERE favorite_type = 'COSMETIC'
                """
                count_sql += " WHERE favorite_type = 'COSMETIC'"

            # favorite_type : 사내문서
            elif favorite_type =='INTERNAL_DOCS':
                sql +=  """
                SELECT * FROM favorites
                    JOIN post ON target_id = post_id
                    JOIN 
                        (SELECT * from document WHERE scope='EXTERNAL' ) document 
                    ON post.document_id = document.document_id
                WHERE favorites.scope='INTERNAL' AND favorite_type != 'NEWS'
                """
                count_sql += " WHERE favorites.scope='INTERNAL' AND favorite_type != 'NEWS'"
           
            # favorite_type : 텍스트
            elif favorite_type =='TEXT':
                sql += " WHERE favorite_type = 'TEXT'"
                count_sql += " WHERE favorite_type = 'TEXT'"
           

            if query:
                sql += " AND (title LIKE %s OR content LIKE %s)"
                count_sql += " AND (title LIKE %s OR content LIKE %s)"
                params.extend([f"%{query}%", f"%{query}%"])
        
            sql += " AND member_id = %s"
            count_sql += " AND member_id = %s"
            params.append(member.get('member_id'))
            
            cursor.execute(count_sql, params) 
            total_count = cursor.fetchone()["COUNT(*)"]

            sql += " ORDER BY favorites.created_at DESC"

            
            offset = (current_page - 1) * item_per_page
            sql += " LIMIT %s OFFSET %s"
            
            params.extend([item_per_page, offset])
            cursor.execute(sql, params)
            result = cursor.fetchall()

            return ListResponse(
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


@router.post("/favorites")
def add_favorites(
    body: FavoriteRequest,
    token: str = Depends(oauth2_scheme),
):
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            member = decode_access_token(token)
            
            cursor.execute(
                'INSERT INTO favorites (scope, favorite_type, target_id, member_id) values (%s, %s, %s, %s)', 
                [body.scope, body.favorite_type, body.target_id, member.get('member_id')]
            )
            conn.commit()
            
            return BaseResponse(code=0, msg="즐겨찾기 추가되었습니다." if cursor.rowcount > 0 else "이미 존재하는 즐겨찾기 입니다")
    finally:
        conn.close()
        
        
# 즐겨찾기 삭제
@router.delete("/favorites")
def remove_favorites(
    body: FavoriteRequest,
    token: str= Depends(oauth2_scheme)
):
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            member = decode_access_token(token)
            
            cursor.execute(
                "DELETE FROM favorites where scope = %s AND favorite_type = %s AND target_id = %s AND member_id = %s", 
                [body.scope, body.favorite_type, body.target_id, member.get('member_id')]
            )
            conn.commit()
            
            return BaseResponse(code=0, msg="즐겨찾기 삭제되었습니다.")
    finally:
        conn.close()