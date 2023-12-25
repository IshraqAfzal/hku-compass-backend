import sys
from loguru import logger
import logging

uvicorn_error = logging.getLogger("uvicorn.error")
uvicorn_error.disabled = True
uvicorn_access = logging.getLogger("uvicorn.access")
uvicorn_access.disabled = True
format = "[{time}]: {level} : {name}:{function}:{line} : {message} {exception}"
logger.remove()
logger.add(sys.stdout, level="TRACE", format=format, enqueue=True, backtrace=True)
# logger.add(sys.stderr, format=format, colorize=True, backtrace=True, diagnose=True)
# logger.add("./logs/files/logs.log", level="TRACE", format=format, rotation="5 MB", serialize=True)

def get_logger():
    return logger