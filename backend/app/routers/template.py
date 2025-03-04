from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.session import get_session 
from schemas.response import BaseResponse
from fastapi.security import  OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()

@router.get("/brands")
def update_my_password(tag: str, token: str= Depends(oauth2_scheme), db: Session = Depends(get_session)):
    brands = db.query().filter(Member.member_id == member.get('member_id')).first()
    
    if not brands:
        return BaseResponse(code=1, msg="현재 비밀번호가 일치하지 않습니다.")

   
    db.commit()
    db.refresh(db_member) 
    return BaseResponse(code=0, msg="변경되었습니다.",)
