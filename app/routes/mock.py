from fastapi import APIRouter, Request, BackgroundTasks
import datetime
from ..mock_data.mock_data_job import push_mock_data

router = APIRouter(
  prefix="/mock",
  tags=["mock"]
)

@router.get("/pushMockReviews")
async def pushMockReviews(request: Request, background_tasks: BackgroundTasks):
  time = str(datetime.datetime.now())
  background_tasks.add_task(push_mock_data, request.app.state.logger, request.app.state.db)
  return "Task started at time " + time + ", check server logs for state."