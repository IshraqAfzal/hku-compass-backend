from fastapi import APIRouter, Request, BackgroundTasks
from ..data.courses_job import general_courses_job
from ..data.profs_job.engineering.cs import collect as csCollect
from ..utils.data.create_driver import create_driver
import datetime

router = APIRouter(
  prefix="/utils",
  tags=["utils"]
)

@router.get("/triggerGeneralCoursesJob")
async def triggerGeneralCoursesJob(request : Request, background_tasks: BackgroundTasks):
  time = str(datetime.datetime.now())
  background_tasks.add_task(general_courses_job, request.app.state.logger, request.app.state.db)
  return "Job started at time " + time + ", check server logs for state."

@router.get("/triggerProfJobCS")
async def triggerProfJobCS(request : Request, background_tasks: BackgroundTasks):
  time = str(datetime.datetime.now())
  background_tasks.add_task(csCollect, request.app.state.db, request.app.state.logger, create_driver())
  return "Job started at time " + time + ", check server logs for state."