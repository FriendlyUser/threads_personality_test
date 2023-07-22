from fastapi import APIRouter, Depends

from app.models import Item

router = APIRouter(prefix="/reports")




@router.get("/")
async def list_items():
    return {"items": "Hello, World!"}


@router.post("/")
async def add_item(item: Item):
    return item
