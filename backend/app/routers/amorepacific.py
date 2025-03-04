from fastapi import APIRouter
router = APIRouter()

@router.get("/")
async def get_brands():
    return {"message": "Get all favorites"}

@router.post("/")
async def add_favorite():
    return {"message": "Add a favorite"}
