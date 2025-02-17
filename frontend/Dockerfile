# Node.js 기반 이미지 사용
FROM node:18

# 작업 디렉토리 설정 (일반적으로 /home/node/app 사용 추천)
WORKDIR /home/node/app

# pnpm 설치
RUN corepack enable && corepack prepare pnpm@latest --activate

# package.json과 pnpm-lock.yaml 먼저 복사
COPY package.json pnpm-lock.yaml ./

# 패키지 설치 (pnpm 사용)
RUN pnpm install

# 모든 파일 복사 (필요한 파일만 복사하려면 .dockerignore 설정)
COPY . .

# Nuxt 빌드
RUN pnpm run build

# 컨테이너 실행 시 Nuxt 서버 시작
CMD ["pnpm", "run", "start"]
