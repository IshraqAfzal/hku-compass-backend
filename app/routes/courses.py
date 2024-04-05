from fastapi import APIRouter, Request, Query
from ..utils.data.create_objectid import create_objectid

router = APIRouter(
  prefix="/courses",
  tags=["Courses"]
)

@router.get("/get-courses")
async def getCourse(request: Request):
  data = request.app.state.db.find_all('courses')
  return {'data' : data}

