from pydantic import BaseModel

class JoinQueueRequest(BaseModel):
    user_id: str

class JoinQueueResponse(BaseModel):
    message: str
    user_id: str
    position: int

class CheckQueueResponse(BaseModel):
    user_id: str
    position: int

class LeaveQueueResponse(BaseModel):
    user_id: str