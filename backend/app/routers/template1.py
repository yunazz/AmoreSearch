from typing import List, Optional
from fastapi import APIRouter, Depends, Query, HTTPException, status
from db.connection import get_connection 
from schemas.response import BaseResponse
from fastapi.security import  OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()


@router.get("/board")
def get_external_boards(
    post_type: str = Query(None), 
    source_name: str = Query(None), 
    query: str = Query(None), 
    current_page: int = Query(1), 
    item_per_page: int = Query(12)
):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * from post_external LEFT JOIN document ON post_external.document_id = document.document_id WHERE 1=1"
            count_sql = "SELECT COUNT(*) FROM post_external WHERE 1=1"
            params = []
        
            if post_type:
                sql += " AND post_type = %s"
                count_sql += " AND post_type = %s"
                params.append(post_type)

            if source_name:
                sql += " AND source_name = %s"
                count_sql += " AND source_name = %s"
                params.append(source_name)

            if query:
                sql += " AND (title LIKE %s OR content LIKE %s)"
                count_sql += " AND (title LIKE %s OR content LIKE %s)"
                params.extend([f"%{query}%", f"%{query}%"])
            
            # 총 개수 조회
            cursor.execute(count_sql, params) 
            total_count = cursor.fetchone()["COUNT(*)"]

            # ORDER BY
            sql += " ORDER BY published_at DESC"
            
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
