from pydantic import BaseModel
from typing import Generic, TypeVar, Optional

T = TypeVar("T") 

class BaseResponse(BaseModel, Generic[T]):
    msg: str = "성공"  # 기본 메시지
    code: int = 0      # 기본 코드 (성공)
    result: Optional[T] = None  # 결과 데이터

    class Config:
        from_attributes = True  # ORM 모델 변환 가능
