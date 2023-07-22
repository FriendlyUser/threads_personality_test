from threads import Threads
from app.models import (
    UserDataResponse,
    # UserThreadResponse,
    # InstagramUser,
    # ThreadsUser,  
    # ThreadsUserData,
    # ThreadsData,
    # ThreadsResponse,
    # UserThreadResponse
)

# if we add auth, move threads function elsewhere
threads = Threads()

def get_id_from_username(username : str) -> int:
    """
    Get the user ID from the given username.

    Parameters:
        username (str): The username of the user.

    Returns:
        int: The ID of the user.
    """
    return threads.public_api.get_user_id(username=username)

def fetch_user_info(user_id: int) -> UserDataResponse:
  user_dict = threads.public_api.get_user(id=user_id)
  for pic in user_dict["hd_profile_pic_versions"]:
    profile_pic = ProfilePic( # assign data directly 
      height=pic["height"],
      width=pic["width"],
      url=pic["url"]
    )
  profile_pics.append(profile_pic)

  user = User(
    is_private=user_dict["is_private"],
    profile_pic_url=user_dict["profile_pic_url"], 
    username=user_dict["username"],
    hd_profile_pic_versions=profile_pics,
    is_verified=user_dict["is_verified"],
    biography=user_dict.get("biography"),
    follower_count=user_dict["follower_count"],
    pk=user_dict["pk"]  
  )
  # Then assign nested data 
  user.hd_profile_pic_versions = profile_pics
  
  data = UserData(user=user)
  return Response(
    data=data,
    extensions=response["extensions"]
  )

def fetch_user_threads(user_id: int)-> dict:
    response = threads.public_api.get_user_threads(id=user_id)
    print(response)
    # if response.get("instagram"):
    #     instagram = InstagramUser(**response["instagram"])
    # else:
    # instagram = InstagramUser()
    
    # threads_user = ThreadsUser(**response["threads"]["data"]["userData"]["user"])
    
    # threads_user_data = ThreadsUserData(user=threads_user)

    # threads_data = ThreadsData(userData=threads_user_data)

    # threads_resp = ThreadsResponse(
    #      data=threads_data,
    #      extensions=response["threads"]["extensions"]
    # )
    return response
    # return UserThreadResponse(
    #     # instagram=instagram,  
    #     threads=threads_resp
    # )