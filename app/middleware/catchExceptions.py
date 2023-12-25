from starlette.requests import Request
from starlette.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware

class ExceptionsMiddleware(BaseHTTPMiddleware):
    async def dispatch(request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            request.state.logger.exception(e)
            return Response("Internal server error", status_code=500)