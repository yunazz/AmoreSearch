# 베이스 이미지로 Python 3.9을 사용
FROM python:3.9-slim

# 작업 디렉터리 설정
WORKDIR /app

# 요구사항 파일을 컨테이너로 복사
COPY requirements.txt .

# 요구사항 설치
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 소스 코드 복사
COPY . .

# 애플리케이션 실행
CMD ["python", "app/main.py"]

# 애플리케이션이 사용하는 포트 노출
EXPOSE 8000
