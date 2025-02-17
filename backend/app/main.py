from app.routes import router
from app.router.member import member_router
from app.router.favorites import favorites_router

from fastapi import FastAPI, Depends, HTTPException, status
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from datetime import datetime,  timedelta, timezone
# from typing import Optional, List
from fastapi.middleware.cors import CORSMiddleware
# from typing import Annotated



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
        
@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
