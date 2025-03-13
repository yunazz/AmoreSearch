## AmoreSearch - backend
[SKN Family AI 캠프 6기] 최종프로젝트 - 아모레서치

pnpm build

pm2 delete client
pm2 start "pnpm run start" --name client


삭제: 
sudo fuser -k 8000/tcp

조회: 
sudo lsof -i :8000

배포: 
nohup uvicorn main:app --host 0.0.0.0 --port 8000 > fastapi.log 2>&1 &

ps aux | grep uvicorn

tail -f fastapi.log

sudo fuser -k 8000/tcp