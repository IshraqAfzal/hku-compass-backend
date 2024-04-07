from fastapi import APIRouter, Request, BackgroundTasks
from ..data.courses_job import general_courses_job
from ..data.profs_job.engineering.cs import collect as csCollect
from ..utils.data.create_driver import create_driver
import datetime

router = APIRouter(
  prefix="/utils",
  tags=["Utility Functions"]
)
# TODO: add passwords for these routes

@router.get("/trigger-general-courses-job")
async def trigger_general_courses_job(request : Request, background_tasks: BackgroundTasks):
  time = str(datetime.datetime.now())
  background_tasks.add_task(general_courses_job, request.app.state.logger, request.app.state.db)
  return "Job started at time " + time + ", check server logs for state."

@router.get("/trigger-prof-job-cs")
async def trigger_prof_job_cs(request : Request, background_tasks: BackgroundTasks):
  time = str(datetime.datetime.now())
  background_tasks.add_task(csCollect, request.app.state.db, request.app.state.logger, create_driver())
  return "Job started at time " + time + ", check server logs for state."

@router.get("/clear-collection-enrollments")
async def clear_collection_enrollments(request : Request, background_tasks: BackgroundTasks):
  request.app.state.db.clear('enrollments')
  return "The collection 'enrollments' was cleared."