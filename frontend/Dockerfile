# Node.js 기반 이미지 사용
FROM node:18

WORKDIR /app 

RUN npm install -g pnpm 

COPY package.json pnpm-lock.yaml ./
RUN pnpm install --frozen-lockfile

COPY . .  

RUN pnpm run build

CMD ["pnpm", "run", "start"]