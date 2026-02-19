from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from schema.chat_request import ChatRequest
from agent import get_response
import logging
import uuid
import uvicorn
from config import env
from contextlib import asynccontextmanager
from db import init_db
from netra import Netra
from netra.instrumentation.instruments import InstrumentSet
from services.simulation import run_simulation

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

Netra.init(
    app_name="Nova Agent",
    block_instruments={InstrumentSet.FASTAPI} #type: ignore
)

Netra.set_tenant_id("Nova")

logging.info("Initialised Netra")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Starting application - initializing database")
    init_db()
    logging.info("Mock DB has been initialized successfully")
    yield
    logging.info("Shutting down application")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
) 

@app.post("/chat")
def chat(chat: ChatRequest, response: Response):
    try:
        thread_id = chat.thread_id or uuid.uuid4().hex
        Netra.set_session_id(thread_id)

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
    
@app.post("/simulation/{dataset_id}")
def start_simulation(dataset_id: str, response: Response):
    try:
        result = run_simulation(dataset_id)
        if not result:
            raise ValueError("Simulation failed")

        return result
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