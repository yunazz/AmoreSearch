from fastapi import APIRouter

member_router = APIRouter(prefix="/api/member", tags=["Member"])

@member_router.get("/")
async def get_members():
    return {"message": "Get all members"}

@member_router.post("/")
async def create_member():
    return {"message": "Create a member"}
