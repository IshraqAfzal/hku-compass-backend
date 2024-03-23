from fastapi import APIRouter, Request, Query
from ..utils.data.create_objectid import create_objectid

router = APIRouter(
  prefix="/courses",
  tags=["courses", "API"]
)

@router.get("/getJustAllCourses")
async def getJustAllCourses(request: Request):
  data = request.app.state.db.find_all('courses')
  return {'data' : data}

@router.get("/getJustAllCoursesTest")
async def getJustAllCoursesTest(request: Request):
  data = request.app.state.db.find_all('courses')[0::500]
  return {'data' : data}

@router.get("/getJustAllCourseSubclasses")
async def getJustAllCoursesTest(request: Request, course_id = Query(0)):
  data = request.app.state.db.find('subclasses', {"COURSE_ID" : create_objectid(course_id)})
  return {'data' : data}

@router.get("/getJustAllCourseSubclassesTest")
async def getJustAllCoursesTest(request: Request):
  print(create_objectid('031406'))
  data = request.app.state.db.find('subclasses', {"COURSE_ID" : create_objectid('031406')})
  return {'data' : data}

