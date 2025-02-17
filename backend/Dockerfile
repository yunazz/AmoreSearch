# Python 기반 FastAPI 실행 환경
FROM python:3.10

# 작업 디렉토리 설정
WORKDIR /home/ubuntu/app

# 의존성 설치
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# FastAPI 코드 복사
COPY backend .

# FastAPI 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]