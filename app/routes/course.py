from fastapi import APIRouter, Request, Query
from ..utils.data.create_objectid import create_objectid

router = APIRouter(
  prefix="/course",
  tags=["Course"]
)

@router.get("/get-course")
async def getCourse(request: Request, course_code = Query(0)):
  data = request.app.state.db.find('courses', {"COURSE_CODE" : course_code})
  return {'data' : data}

@router.get("/get-subclasses")
async def getCourseSubclasses(request: Request, course_id = Query(0)):
  data = request.app.state.db.find('subclasses', {"COURSE_ID" : create_objectid(course_id)})
  return {'data' : data}

@router.get("/get-enrollments")
async def getCourseEnrollments(request: Request, course_id = Query(0)):
  data = request.app.state.db.find('enrollments', {"COURSE_ID" : create_objectid(course_id)})
  return {'data' : data}

@router.get("/get-sftl")
async def getCourseSFTL(request: Request, course_id = Query(0)):
  data = request.app.state.db.find('sftl', {"COURSE_ID" : create_objectid(course_id)})
  return {'data' : data}

@router.get("/get-reviews")
async def getCourseReviews(request: Request, course_id = Query(0)):
  data = request.app.state.db.find('course_reviews', {"COURSE_ID" : create_objectid(course_id)})
  return {'data' : data}