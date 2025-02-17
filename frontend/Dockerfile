# Node.js 기반 이미지 사용
FROM node:18

# 작업 디렉토리 설정
WORKDIR /frontend


# pnpm 설치
RUN corepack enable && corepack prepare pnpm@latest --activate

# package.json과 pnpm-lock.yaml 먼저 복사
COPY frontend/package.json frontend/pnpm-lock.yaml ./

# 패키지 설치
RUN pnpm install

# 모든 파일 복사
COPY . /frontend

# Nuxt 빌드
RUN pnpm run build

# 컨테이너 실행 시 Nuxt 서버 시작
CMD ["pnpm", "run", "start"]
