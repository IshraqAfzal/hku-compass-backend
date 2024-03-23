from fastapi import APIRouter, Request, BackgroundTasks
from ..data.courses_job import general_courses_job
import asyncio
import datetime

router = APIRouter(
  prefix="/utils",
  tags=["utils"]
)

@router.get("/triggerGeneralCoursesJob")
async def triggerGeneralCoursesJob(request : Request, background_tasks: BackgroundTasks):
  time = str(datetime.datetime.now())
  # asyncio.create_task(general_courses_job(request.app.state.logger, request.app.state.db))
  background_tasks.add_task(general_courses_job, request.app.state.logger, request.app.state.db)
  return "Job started at time " + time + ", check server logs for state."