from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth,member, post

app = FastAPI()

    
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(member.router, prefix="/api/member", tags=["member"])
app.include_router(post.router, prefix="/api/post", tags=["post"])