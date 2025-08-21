import redis
from app.core.settings import settings

_redis_client = redis.Redis.from_url(settings.redis_url)

def get_redis_client():
    return _redis_client