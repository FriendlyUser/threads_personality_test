from fastapi import APIRouter, Depends
from threads import Threads
from app.models import UserIdentity, UserDataResponse, UserThreadResponse, UserThreadResponse
from app.services.parse_threads import get_id_from_username, fetch_user_info, fetch_user_threads

router = APIRouter(prefix="/threads")
threads = Threads()
@router.get("/username/{username}")
async def get_user(username: str) -> UserIdentity:
    """
    Get a user by their username.

    Parameters:
    - username: A string representing the username of the user to retrieve.

    Returns:
    - user: An instance of the User class representing the user with the given username.
    """
    user_id = get_id_from_username(username)
    user = UserIdentity(id=user_id, username=username)
    return user

@router.get("/userid/{userid}")
def get_user_info(userid: int) -> UserDataResponse:
    user = fetch_user_info(userid)
    return user

@router.get("/user_threads/{userid}")
def get_user_threads(userid: int) -> UserDataResponse:
    user_threads = fetch_user_threads(userid)
    return user_threads
