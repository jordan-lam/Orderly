from app.core.redis_client import get_redis_client

QUEUE_NAME = "buyer_queue"


def join_queue(user_id: str) -> int:
    """
    Add the user to the queue and return their position
    """
    client = get_redis_client()

    client.rpush(QUEUE_NAME, user_id)

    position = client.llen(QUEUE_NAME)

    return position


def check_position(user_id: str) -> int:
    """
    Check position of user in line and return their position
    """
    client = get_redis_client()

    queue = client.lrange(QUEUE_NAME, 0, -1)
    queue = [u.decode("utf-8") for u in queue]

    try:
        return queue.index(user_id) + 1
    except ValueError:
        return None


def next_user() -> str:
    """
    Pop the next user off the list and return user_id
    """

    client = get_redis_client()

    user = client.lpop(QUEUE_NAME)

    if user is not None:
        return user.decode("utf-8")
    return None
