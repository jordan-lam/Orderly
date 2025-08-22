import os

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
FASTAPI_HOST = os.getenv("FASTAPI_HOST", "0.0.0.0")
FASTAPI_PORT = int(os.getenv("FASTAPI_PORT", 8000))