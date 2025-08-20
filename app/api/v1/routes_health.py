from fastapi import APIRouter
from app.core.redis_client import get_redis_client
router = APIRouter()

@router.get("/")
async def health_check():
    return {"status": "ok"}


@router.get("/redis-test")
async def redis_test():
    client = get_redis_client()
    try:
        pong = client.ping()
        return {"redis_ping": pong}
    except Exception as e:
        return {"error": str(e)}