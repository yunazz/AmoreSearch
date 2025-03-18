from fastapi import APIRouter, Query
from typing import Optional
from db.connection import get_connection 
from schemas.response import BaseResponse
from fastapi.responses import StreamingResponse
from core.llm import AISearch, IntegrationSearch, RagSearch

import asyncio
router = APIRouter()

    
@router.get("/brand")
async def search_brand(brand_kor:str, query: str ):
    try:
        question = f"""
            너는 아모레퍼시픽의 전문 AI 컨설턴트입니다. 나는 아모레퍼시픽 직원입니다.
            {brand_kor}에 대해서 질문할 내용이 있습니다. {query}. 
            
            대답을 할 때에는 소개는 생략했으면 좋겠습니다.
            줄바꿈은 <br/> 로 대체해줬으면 좋겠고, 굵게 표시할 문자는 <b></b>로 감싸주었으면 좋겠습니다.
        """
    
        return StreamingResponse(AISearch.search(question), media_type="text/plain")
    except:
        return BaseResponse(code=1, msg="조회 실패")

@router.get("/ai")
async def search_ai(query: str):
    """FastAPI 엔드포인트: AI 검색 실행"""
    try:
        return StreamingResponse(IntegrationSearch.search(query), media_type="application/json")

    except Exception as e:
        return BaseResponse(code=1, msg="조회 실패")
    
@router.get("/references")
def search_ai(query: str):
    """검색창 우측에 연관된 문서를 띄우기 위해 조회하는 API"""
    try:
        result =  RagSearch.search(query, tag)

        if result is None:
            return BaseResponse(code=1, msg="조회 실패")
        
        return BaseResponse(code=0, msg="조회 성공", result=result)

    except Exception as e:
        return BaseResponse(code=1, msg="조회 실패")
    
@router.get("/category")
def search_ai(query: str):
    """검색시 선택한 태그와 관련된 내용을 보여주기 위해 조회하는 API"""
    try:
        result =  RagSearch.search(query, tag)

        if result is None:
            return BaseResponse(code=1, msg="조회 실패")
        
        return BaseResponse(code=0, msg="조회 성공", result=result)

    except Exception as e:
        return BaseResponse(code=1, msg="조회 실패")
    