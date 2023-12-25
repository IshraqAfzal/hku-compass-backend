from dotenv import load_dotenv
from pathlib import Path
import threading

import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from middleware.catchExceptions import ExceptionsMiddleware
from logs.loggerReqMiddleware import ReqLogMiddleware
from logs.logger import get_logger
from db.dbMiddleware import DBMiddleware
from db.client import MongoDBClient

from routes import test
from data import router as dataRouter, data_collection_job

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)
logger = get_logger()
# db = MongoDBClient()
db = None
data_thread = threading.Thread(target=data_collection_job, args=(db,logger))

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.logger.info("Creating Server Context.")
    app.state.db = db
    app.state.logger = logger
    data_thread.start()
    app.state.logger.info("Created Server Context sucessfully.")
    yield
    app.state.db.close()
    app.state.logger.info("Server stopped successfully.")

app = FastAPI(lifespan=lifespan)

app.add_middleware(ExceptionsMiddleware) # This has to be on top of all other middleware
app.add_middleware(ReqLogMiddleware)
app.add_middleware(DBMiddleware)

app.include_router(dataRouter)
app.include_router(test.router) 

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="warning")