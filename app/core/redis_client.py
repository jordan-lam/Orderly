import redis
from app.core.settings import REDIS_URL

_redis_client = redis.Redis.from_url(REDIS_URL)


def get_redis_client():
    return _redis_client