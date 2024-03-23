from dotenv import load_dotenv
from pathlib import Path
from fastapi import FastAPI, Depends
from fastapi.openapi.utils import get_openapi
from contextlib import asynccontextmanager
from .middleware.catchExceptions import ExceptionsMiddleware
from .middleware.requestLogging import ReqLogMiddleware
from .logs.logger import get_logger
from .middleware.dbConnectivity import DBMiddleware
from .db.client import MongoDBClient
from .routes import test, courses, docs, utils
from .data import router as dataRouter
from .data.data_collection_job import DataJob

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)
logger = get_logger()
server_db_instance = MongoDBClient(name='SERVER-DB')
data_collection_job = DataJob(logger, server_db_instance)

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.logger = logger
    app.state.logger.info("Creating Server Context.")
    app.state.db = server_db_instance
    app.state.logger.info("Created Server Context sucessfully.")
    data_collection_job.run()
    yield
    app.state.db.close()
    data_collection_job.stop()
    app.state.logger.info("Server stopped successfully.")

app = FastAPI(lifespan=lifespan,     
            docs_url=None,
            redoc_url=None,
            openapi_url = None)

@app.get("/openapi.json", include_in_schema=False)
async def openapi(username: str = Depends(docs.get_current_username)):
    return get_openapi(title=app.title, version=app.version, routes=app.routes)

app.add_middleware(ExceptionsMiddleware) # This has to be on top of all other middleware
app.add_middleware(ReqLogMiddleware)
app.add_middleware(DBMiddleware)

app.include_router(dataRouter)
app.include_router(test.router) 
app.include_router(courses.router) 
app.include_router(docs.router) 
app.include_router(utils.router) 
