from typing import List, Optional
from fastapi import APIRouter, Query
from db.connection import get_connection 
from schemas.response import BaseResponse
from fastapi.security import  OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()

@router.get("/brands")
def get_boards():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM brand WHERE brand_kor != '아모레퍼시픽'"
            params = []

            cursor.execute(sql, params)
            brands = cursor.fetchall()

            return BaseResponse(code=0, msg="조회 성공", result=brands)

    finally:
        conn.close()       