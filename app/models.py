from pydantic import BaseModel
from typing import Optional, List
class Item(BaseModel):
    name: str
    description: str | None = None


class UserIdentity(BaseModel):
    id: int
    username: str


class ProfilePic(BaseModel):
    height: int
    url: str
    width: int

class User(BaseModel):
    is_private: bool 
    profile_pic_url: str
    username: str
    hd_profile_pic_versions: List[ProfilePic]
    is_verified: bool
    biography: Optional[str] = None
    biography_with_entities: Optional[str] = None
    follower_count: int
    pk: str

class UserData(BaseModel):
    user: User

class Response(BaseModel):
    data: UserData
    extensions: dict