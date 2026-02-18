from fastapi import FastAPI, Response
from schema.chat_request import ChatRequest
from agent import get_response
import logging
import uuid
import uvicorn
from config import env
from contextlib import asynccontextmanager
from db import init_db, db

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Starting application - initializing database")
    init_db()
    logging.info("Mock DB has been initialized successfully")
    yield
    logging.info("Shutting down application")

app = FastAPI(lifespan=lifespan)

@app.post("/chat")
def chat(chat: ChatRequest, response: Response):
    try:
        thread_id = chat.thread_id or uuid.uuid4().hex

        return {
            "response": get_response(chat.prompt, thread_id),
            "thread_id": thread_id
        }
    except Exception as e:
        logging.error(msg=e)
        response.status_code = 500
        return {
            "error": "An error occurred"
        }
    
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=env.ENVIRONMENT == "dev",
        log_level="info"
    )