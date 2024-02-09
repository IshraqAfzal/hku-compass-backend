from starlette.middleware.base import BaseHTTPMiddleware
import ultraimport
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

logs = ultraimport('__dir__/../logs/logger.py')
logger = logs.get_logger()

class DBMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = JSONResponse(
            jsonable_encoder(
                {'body' : None, 'err' : "Database connection unsucessful."}
            )
        )
        if (request.app.state.db.connection_status):
            response = await call_next(request)
        else:
            request.app.state.logger.info(
                "DB Middleware: Database is not connected.",
            )
            request.app.state.db.connect()
        return response