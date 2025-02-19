# Node.js 기반 이미지 사용
FROM node:18

WORKDIR /app 

# 패키지 매니저 설치
RUN corepack enable && corepack prepare pnpm@latest --activate

# package.json만 복사하여 캐시 활용
COPY package.json ./
RUN pnpm install --frozen-lockfile

# 나머지 파일 복사
COPY . .  

# 빌드 실행
RUN pnpm run build

# 컨테이너 실행 명령어
CMD ["pnpm", "run", "start"]