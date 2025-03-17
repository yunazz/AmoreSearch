from fastapi import APIRouter, Query
from typing import Optional
from db.connection import get_connection 
from schemas.response import BaseResponse
from fastapi.responses import StreamingResponse
from core.llm import AISearch, IntegrationSearch
import asyncio
router = APIRouter()

async def ai_response_generator(query: str):
    """AI 응답을 실시간으로 스트리밍하는 제너레이터"""
    async for chunk in IntegrationSearch.search(query):  
        yield chunk + "\n"  # 줄바꿈 추가하여 스트리밍 효과 극대화
        await asyncio.sleep(0.1)  # 🔥 너무 빠른 스트리밍을 방지
        
@router.get("/brand")
async def search_brand( brand_kor:str, query: str ):
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
        response = await IntegrationSearch.search(query)
        # return StreamingResponse(ai_response_generator(query), media_type="text/plain")
        return BaseResponse(code=0, msg="조회 성공", result=response)
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
       
        return BaseResponse(code=1, msg="조회 실패")