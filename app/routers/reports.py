from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.services.parse_threads import parse_threads

router = APIRouter(prefix="/reports")


class Item(BaseModel):
    name: str
    description: str | None = None


@router.get("/")
async def list_items():
    return {"items": "Hello, World!"}


@router.post("/")
async def add_item(item: Item):
    return item
