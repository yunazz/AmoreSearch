from fastapi import APIRouter

favorites_router = APIRouter(prefix="/api/favorites", tags=["Favorites"])

@favorites_router.get("/")
async def get_favorites():
    return {"message": "Get all favorites"}

@favorites_router.post("/")
async def add_favorite():
    return {"message": "Add a favorite"}
