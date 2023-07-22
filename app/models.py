from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None


class User(BaseModel):
    id: int
    username: str