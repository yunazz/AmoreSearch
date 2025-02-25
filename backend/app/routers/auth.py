import os
import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

load_dotenv()
router = APIRouter()

# 환경 변수 가져오기
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 30))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_jwt_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + expires_delta 
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

fake_members_db = {
    "2045910583": {
        "member_id": 1,
        "emp_no": "2045910583",
        "role": 2,
        "name": "홍길동",
        "company_affiliation": "아모레퍼시픽",
        "birth_date": "1995-01-01",
        "phone": "010-4470-1111",
        "hire_date": "2020-01-01",
        "employment_status": "재직",
        "position": "사원",
        "department": "HR팀",
        "password": pwd_context.hash("testpassword")
    }
}

def verify_password(plain_password, password):
    return pwd_context.verify(plain_password, password)

def authenticate_member(emp_no: str, password: str):
    member = fake_members_db.get(emp_no)
    if not member or not verify_password(password, member["password"]):
        return None
    return member

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now().astimezone() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    member = authenticate_member(form_data.username, form_data.password)
    if not member:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="아이디 또는 비밀번호를 확인해 주세요." )

    access_token = create_access_token(data={key: member[key] for key in member if key != "password"})

    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me")
def read_members_me(token: str= Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"result": payload, "code" : 0, "detail": '성공'}
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="아이디 또는 비밀번호를 확인해 주세요.")
    except jwt.DecodeError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="유효하지 않은 토큰입니다.")