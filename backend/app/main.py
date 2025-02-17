from fastapi import FastAPI, Depends, HTTPException, status
# from jose import JWTError, jwt
# from passlib.context import CryptContext
# from datetime import datetime,  timedelta, timezone
# from typing import Optional, List
# from typing import Annotated



app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
