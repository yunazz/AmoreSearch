from fastapi import APIRouter, Query
from typing import Optional
from db.connection import get_connection 
from schemas.response import BaseResponse
from core.llm import AISearch
import re

router = APIRouter()

def convert_markdown_bold_to_html(text):
    """Markdown의 **텍스트** 형식을 <b>텍스트</b>로 변환"""
    return re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)
def convert_linebreak_to_html(text):
    """Markdown의 줄바꿈 n을 <br/>로 변환"""
    return re.sub(r"\n", r"</br>", text)

@router.get("/brand")
def search_brand( brand_kor:str, query: str ):
    try:
        openai = AISearch()
        question = f'너는 아모레퍼시픽의 전문 AI 컨설턴트야. 나는 아모레퍼시픽 직원이야. 상사가 설명해주듯이 설명해주었으면 좋겠어. {brand_kor}에 대해서 질문할 내용이 있어. {query}'
            
        response = openai.search(question)
        
        content = convert_markdown_bold_to_html(response.content)
        content = convert_linebreak_to_html(content)
        
        return BaseResponse(code=0, msg="조회 성공", result=content)
    
        # conn = get_connection()
        # with conn.cursor() as cursor:
        #     sql = """
        #     """
        #     cursor.execute(sql )
        #     result = cursor.fetchall()

        #     return BaseResponse(
        #         code=0,
        #         msg="조회 성공",
        #         result=result,
        #     )
    except:
        return BaseResponse(code=1, msg="조회 실패")
    # finally:
    #     # conn.close()

@router.get("/ai")
def search_ai(query: str):
    try:
        openai = AISearch()
        response = openai.invoke(query)
        
        return BaseResponse(code=1, msg="조회 실패", result=response)
        # conn = get_connection()
        # with conn.cursor() as cursor:
        #     sql = """
        #     """
        #     cursor.execute(sql )
        #     result = cursor.fetchall()

        #     return BaseResponse(
        #         code=0,
        #         msg="조회 성공",
        #         result=result,
        #     )
        pass
    finally:
        # conn.close()
        pass

    return BaseResponse(code=1, msg="조회 실패")