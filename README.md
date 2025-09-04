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

1. **Queue Safeguards**  
   - Add timestamps for analytics and auditing.  
   - Prevent “double dipping” (users joining multiple times).

2. **Dashboard / Admin Interface**  
   - Monitor queue in real-time, manage flow, and visualize statistics.

---

## Getting Started (MVP)

1. **Clone the repository:**
   ```bash
   git clone <repo_url>
   cd Orderly
   ```

2. **Install Docker:**
   Install Docker from https://docs.docker.com/engine/install/

3. **Create environment file:**
   Create a `.env` file in the project root with the following content:
   ```bash
   REDIS_URL=redis://redis:6379
   FASTAPI_HOST=0.0.0.0
   FASTAPI_PORT=8000
   ```

4. **Run the application:**
   
   **Startup:**
   ```bash
   docker-compose up --build
   ```
   
   **Shutdown:**
   ```bash
   docker-compose down
   ```

5. **Test the API:**
   ```bash
   curl http://localhost:8000/api/v1/health/
   ```
