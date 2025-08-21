from fastapi import APIRouter, HTTPException
from app.core.redis_client import get_redis_client
from app.models.queue import JoinQueueRequest, JoinQueueResponse, CheckQueueResponse, LeaveQueueResponse
from app.services.queue_manager import join_queue, check_position, next_user

router = APIRouter()
    
# Add a user to the queue
@router.post("/join", response_model=JoinQueueResponse)
def join_line(request: JoinQueueRequest):
    position = join_queue(request.user_id)
    return JoinQueueResponse(message="Joined queue",user_id=request.user_id, position=position)
    

# Check position in queue
@router.get("/status/{user_id}", response_model=CheckQueueResponse)
def check_status(user_id: str):
    position = check_position(user_id)
    if position is not None:
        return CheckQueueResponse(user_id=user_id, position=position)
    else:
        raise HTTPException(status_code=404, detail="User not found.")

# Serve the next in line
@router.post("/next", response_model=LeaveQueueResponse)
def serve_next():
    user_id = next_user()
    if user_id is not None:
        return LeaveQueueResponse(user_id=user_id)
    else:
        raise HTTPException(status_code=400, detail="Queue is empty")