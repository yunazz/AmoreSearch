from fastapi import APIRouter, Query
from typing import Optional
from db.connection import get_connection 
from schemas.response import BaseResponse
from fastapi.responses import StreamingResponse
from core.llm import AISearch
import re

router = APIRouter()

# def convert_markdown_bold_to_html(text):
#     """Markdown의 **텍스트** 형식을 <b>텍스트</b>로 변환"""
#     return re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)
# def convert_linebreak_to_html(text):
#     """Markdown의 줄바꿈 n을 <br/>로 변환"""
#     return re.sub(r"\n", r"</br>", text)

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

    #     openai = AISearch()
            
    #     # response = openai.search(question)
        
    #     # content = convert_markdown_bold_to_html(response.content)
    #     # content = convert_linebreak_to_html(content)
        
    #     return StreamingResponse(openai.generate_response(question), media_type="text/plain")
    #     # return BaseResponse(code=0, msg="조회 성공", result=content)
    
    #     # conn = get_connection()
    #     # with conn.cursor() as cursor:
    #     #     sql = """
    #     #     """
    #     #     cursor.execute(sql )
    #     #     result = cursor.fetchall()

    #     #     return BaseResponse(
    #     #         code=0,
    #     #         msg="조회 성공",
    #     #         result=result,
    #     #     )
    except:
        return BaseResponse(code=1, msg="조회 실패")
    # # finally:
    # #     # conn.close()

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