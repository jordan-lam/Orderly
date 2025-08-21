from fastapi import FastAPI
from app.api.v1 import routes_health, routes_queue

app = FastAPI(title="Orderly Queue System")

app.include_router(routes_queue.router, prefix="/api/v1/queue", tags=["queue"])
app.include_router(routes_health.router, prefix = "/api/v1/health", tags=["health"])