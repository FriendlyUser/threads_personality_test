from fastapi import APIRouter, Depends

from app.models import UserIdentity
from app.services.parse_threads import get_id_from_username

router = APIRouter(prefix="/threads")

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

@router.get("/userid/{user_id}")
def get_user_data(user_id: int) -> Response:
  
  response = threads.public_api.get_user(id=user_id)
  
  user_dict = response["data"]["userData"]["user"]
  
  profile_pics = [ProfilePic(**pic) for pic in user_dict["hd_profile_pic_versions"]]
  
  user = User(
    hd_profile_pic_versions=profile_pics,
    **user_dict
  )
  
  data = UserData(user=user)

  return Response(
    data=data,
    extensions=response["extensions"]
  )