from threads import Threads

def get_id_from_username(username : str) -> int:
    """
    Get the user ID from the given username.

    Parameters:
        username (str): The username of the user.

    Returns:
        int: The ID of the user.
    """
    return threads.public_api.get_user_id(username=username)