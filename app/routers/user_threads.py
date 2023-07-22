from fastapi import APIRouter, Depends

from app.models import User
from app.services.parse_threads import get_id_from_username

router = APIRouter(prefix="/threads")

@router.get("/{username}")
async def get_user(username: str) -> User:
    """
    Get a user by their username.

    Parameters:
    - username: A string representing the username of the user to retrieve.

    Returns:
    - user: An instance of the User class representing the user with the given username.
    """
    user_id = get_id_from_username(username)
    user = User(id=user_id, username=username)
    return user