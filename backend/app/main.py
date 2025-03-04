from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from schemas.response import BaseResponse
from fastapi.middleware.cors import CORSMiddleware
from routers import auth,member, amorepacific

app = FastAPI()

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=BaseResponse(msg=exc.detail, code=exc.status_code, result=None).model_dump(),
    )
    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
        
@app.get("/")
def read_root():
    return {"Hello": "World!"}

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(member.router, prefix="/api/member", tags=["member"])
app.include_router(amorepacific.router, prefix="/api/favorites", tags=["favorites"])