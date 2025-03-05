from typing import List, Optional
from fastapi import APIRouter, Depends, Query, HTTPException, status
from db.connection import get_connection 
from schemas.response import BaseResponse
# from schemas.amorepacific import BrandRequest
from fastapi.security import  OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

from model import Brand
from schemas.amorepacific import BrandResponse

router = APIRouter()


@router.get("/brands")
def get_brands(query: str = Query(None), ctgry: str = Query(None)):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM brand WHERE brand_kor != '아모레퍼시픽'")
            brands = cursor.fetchall()
            return BaseResponse(code=0, msg="조회 성공", result=brands)
        return users
    finally:
        conn.close()
        return BaseResponse(code=1, msg="조회 실패")


@router.get("/board")
def get_boards(
    post_type: str = Query(None), 
    post_ctgry: str = Query(None), 
    query: str = Query(None), 
    page_no: int = Query(1), 
    page_per_group: int = Query(12)
):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            # BRAND 유형의 게시글 조회
            if post_type == "BRAND":
                sql = "SELECT * FROM brand WHERE brand_kor != '아모레퍼시픽'"
                params = []

                if post_ctgry:
                    sql += " AND brand_ctgry = %s"
                    params.append(post_ctgry)

                cursor.execute(sql, params)
                brands = cursor.fetchall()

                return BaseResponse(code=0, msg="조회 성공", result=brands)

            # 일반 게시글 (post) 조회
            else:
                sql = ''
                if post_type=='NEWS':
                    sql += "SELECT p.*, pi.image_url FROM post p LEFT JOIN post_image pi ON p.post_id = pi.post_id AND pi.image_type = 'THUMBNAIL' WHERE 1=1"
                elif post_type=='REPORT':
                    sql += "SELECT p.*, d.original_file_url as file_url FROM post p LEFT JOIN document d ON p.document_id = d.document_id WHERE 1=1"
                else:
                    sql = "SELECT * FROM post WHERE 1=1"
                    
                count_sql = "SELECT COUNT(*) FROM post WHERE 1=1"
                params = []

                if post_type:
                    sql += " AND post_type = %s"
                    count_sql += " AND post_type = %s"
                    params.append(post_type)

                if post_ctgry:
                    sql += " AND p.post_ctgry = %s"
                    count_sql += " AND post_ctgry = %s"
                    params.append(post_ctgry)

                if query:
                    sql += " AND (title LIKE %s OR content LIKE %s)"
                    count_sql += " AND (title LIKE %s OR content LIKE %s)"
                    params.extend([f"%{query}%", f"%{query}%"])
                
                # 총 개수 조회
                cursor.execute(count_sql, params) 
                total_count = cursor.fetchone()["COUNT(*)"]

                # ORDER BY
                sql += " ORDER BY p.created_at DESC"
                
                # 페이징 적용
                offset = (page_no - 1) * page_per_group
                sql += " LIMIT %s OFFSET %s"
                params.extend([page_per_group, offset])

                # 데이터 조회
                cursor.execute(sql, params)
                result = cursor.fetchall()

                return BaseResponse(
                    code=0,
                    msg="조회 성공",
                    result=result,
                    paging={
                        "total_rows": total_count,
                        "page_no": page_no,
                        "page_per_group": page_per_group,
                    }
                )

    finally:
        conn.close()

    return BaseResponse(code=1, msg="조회 실패")
