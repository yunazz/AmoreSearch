from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()


@router.post("/login/", tags=["login"])
async def login_member():
    return [{"message": "로그인되었습니다."}]


app.include_router(router)