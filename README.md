# Orderly

## Virtual Waiting Room & Purchase Queue System

**Orderly** is a scalable virtual waiting room and purchase queue system built with **FastAPI** and **Redis**.  
It is designed to handle high-traffic scenarios for limited-inventory items by queueing users fairly, releasing them at a controlled rate, and preventing overselling.

---

## Current MVP Functionality

The current version implements **3 core endpoints**:

| HTTP Method | Endpoint                        | Description |
|------------|---------------------------------|-------------|
| POST       | `/api/v1/queue/join`            | Add a user to the Redis queue using `user_id` |
| GET        | `/api/v1/queue/status/{user_id}` | Check the current position of a `user_id` in the queue |
| POST       | `/api/v1/queue/next`            | Remove the user at the front of the queue and return their `user_id` |

---

## Planned Features / Next Steps

1. **Dockerization**  
   - Containerize FastAPI + Redis for easy deployment.

2. **Queue Safeguards**  
   - Add timestamps for analytics and auditing.  
   - Prevent “double dipping” (users joining multiple times).

3. **Dashboard / Admin Interface**  
   - Monitor queue in real-time, manage flow, and visualize statistics.

---

## Getting Started (MVP)

1. Clone the repository:  
git clone <repo_url>
2. Install dependencies:
pip install -r requirements.txt
3. Start Redis (via Docker or local instance) and run Fast API
uvicorn app.main:app -reload
