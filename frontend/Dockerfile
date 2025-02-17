# Node.js 기반 이미지 사용
FROM node:18

WORKDIR /app 

# pnpm 설치
RUN corepack enable && corepack prepare pnpm@latest --activate

COPY package.json pnpm-lock.yaml ./

RUN pnpm install

COPY . .  

RUN pnpm run build

CMD ["pnpm", "run", "start"]