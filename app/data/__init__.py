from fastapi import APIRouter
from .courses import all_courses_job, router as coursesRouter
from .engineering import router as enggRouter, job as enggJob
import os

router = APIRouter(
  prefix="/data",
  tags=["data"]
)

router.include_router(coursesRouter)
router.include_router(enggRouter)

def dummy():
  print()

def recurring_job(db, logger):
  logger.info("Starting job")
  enggJob(db, logger, dummy)

async def data_collection_job(db, logger):
  logger.info("Starting job")
  try:
    # if (os.getenv("COURSE_FRAME_JOB") == "True"):
    all_courses_job(db, logger)
    # recurring_job(db, logger)
  except Exception as e:
    logger.exception(e)
