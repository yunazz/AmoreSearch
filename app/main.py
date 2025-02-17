from app.routes import router
from app.router.member import member_router
from app.router.favorites import favorites_router

from fastapi import FastAPI, Depends, HTTPException, status
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from datetime import datetime,  timedelta, timezone
# from typing import Optional, List
# from fastapi.middleware.cors import CORSMiddleware
# from typing import Annotated

app = FastAPI()
        
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


app = FastAPI()

# 모든 라우터 등록
app.include_router(member_router)
app.include_router(favorites_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
