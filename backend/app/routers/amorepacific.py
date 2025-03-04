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
def get_brands(query: str = Query(None), brand_ctgry: str = Query(None),page_no: int = Query(1),page_per_group: int = Query(10)):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM brand WHERE brand_kor != '아모레퍼시픽'")
            brands = cursor.fetchall()
            return BaseResponse(code=0, msg="조회 성공", result=brands)
        return users
    finally:
        conn.close()

    
    # query = db.query(Brand).filter(Brand.brand_ctgry != "아모레퍼시픽")

    # # brand_ctgry가 제공되었을 경우 추가 필터링
    # if brand_ctgry:
    #     query = query.filter(Brand.brand_ctgry == brand_ctgry)
        
    # brands = query.all()

    # return BaseResponse(code=0, msg="조회 성공", result=brands)