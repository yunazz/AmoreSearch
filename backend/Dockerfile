# 1. Python 베이스 이미지 설정
FROM python:3.9-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 의존성 파일을 컨테이너에 복사
COPY requirements.txt ./

# 4. 의존성 설치 (캐시를 사용하지 않도록 설정)
RUN pip install --no-cache-dir -r requirements.txt

# 5. backend 디렉토리 전체를 /app으로 복사
COPY ./backend /app

# 6. FastAPI 서버 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# 7. 컨테이너 외부와 통신할 포트 개방
EXPOSE 8000
