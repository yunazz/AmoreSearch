# # Node.js 기반 이미지 사용
# FROM node:18

# WORKDIR /app 

# RUN npm install -g pnpm

# COPY package.json pnpm-lock.yaml ./

# RUN pnpm install

# COPY . .  

# RUN pnpm run build

# CMD ["pnpm", "run", "start"]


# Node.js LTS 버전 사용
FROM node:lts

# 작업 디렉토리 설정
WORKDIR /app

# 패키지 매니저 업데이트 및 필요 패키지 설치
RUN npm install -g pnpm pm2

# 프로젝트 파일 복사
COPY package.json pnpm-lock.yaml ./
RUN pnpm i

# 프로젝트 전체 복사
COPY . .

# Nuxt 빌드 실행
RUN pnpm run build

# PM2로 Nuxt 서버 실행
CMD ["pm2-runtime", "start", "ecosystem.config.mjs"]
