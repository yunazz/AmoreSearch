FROM python:3.9-slim

WORKDIR /app

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 프로젝트 파일 복사
COPY . .

# uvicorn으로 FastAPI 실행
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]