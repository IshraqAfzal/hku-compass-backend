from fastapi import APIRouter
from .courses import get_all_courses
from .db import write

router = APIRouter(
  prefix="/courses",
  tags=["courses"]
)

last_courses = []

def all_courses_job(db, logger):
  logger.info("Starting job")
  global last_courses
  courses = get_all_courses()
  # write(db, logger, courses)
  last_courses = courses


@router.get("/")
async def helloworld():
  global last_courses
  return last_courses