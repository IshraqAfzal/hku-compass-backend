from fastapi import APIRouter, Request, Query
from ..utils.data.create_objectid import create_objectid
import random
from bson import ObjectId

router = APIRouter(
  prefix="/courses",
  tags=["Courses"]
)

@router.get("/get-all")
async def get_all(request: Request):
  data = request.app.state.db.find_all('courses')
  for i in data:
    del i["ACAD_GROUP"]
    del i["TNL"]
  return {'data' : data}

@router.get("/get")
async def get(request: Request, course_id = Query(0)):
  data = request.app.state.db.find('courses', {"COURSE_ID" : create_objectid(course_id)})
  for i in data:
    del i['ACAD_GROUP']
  return {'data' : data}

@router.get("/get-subclasses")
async def get_subclasses(request: Request, course_id = Query(0)):
  subclasses = request.app.state.db.find('subclasses', {"COURSE_ID" : create_objectid(course_id)})
  enrollments = request.app.state.db.find('enrollments', {"COURSE_ID" : create_objectid(course_id)})
  data = {
    "subclasses" : subclasses,
    "enrollments" : enrollments
  }
  return {'data' : data}

@router.get("/get-enrollments")
async def get_enrollments(request: Request, course_id = Query(0)):
  data = request.app.state.db.find('enrollments', {"COURSE_ID" : create_objectid(course_id)})
  return {'data' : data}

@router.get("/get-sftl")
async def get_sftl(request: Request, course_id = Query(0)):
  data = request.app.state.db.find('sftl', {"COURSE_ID" : create_objectid(course_id)})
  return {'data' : data}

@router.get("/get-reviews")
async def get_reviews(request: Request, course_id = Query(0)):
  data = request.app.state.db.find('course_reviews', {"COURSE_ID" : create_objectid(course_id)})
  for datum in data:
    # TODO: aggregate and fetch user data
    # TODO: aggregate and fetch instructor details
    # Placeholder for mock data
    if course_id == "030837":
      prof = request.app.state.db.find('professors', {"PROF_ID" : create_objectid('atctam_cs')})[0]
      # TODO: store it in the comment too?
      datum['INSTRUCTOR_NAME'] = prof['FULLNAME']
      datum['USER_FACULTY'] = "Engineering"
      datum['USER_DEPARTMENT'] = "Computer Science"
      datum['USER_PROFILE_PIC'] = random.randint(0, 3)
    pass
  return {'data' : data}

@router.get("/get-reviews-by-user")
async def get_reviews_by_user(request: Request, course_id = Query(0), user_id = Query(1)):
  data = request.app.state.db.find('course_reviews', {"COURSE_ID" : create_objectid(course_id), "USER_ID" : ObjectId(user_id)})
  for datum in data:
    # TODO: aggregate and fetch user data
    # TODO: aggregate and fetch instructor details
    # Placeholder for mock data
    if course_id == "030837":
      prof = request.app.state.db.find('professors', {"PROF_ID" : create_objectid('atctam_cs')})[0]
      # TODO: store it in the comment too?
      datum['INSTRUCTOR_NAME'] = prof['FULLNAME']
      datum['USER_FACULTY'] = "Engineering"
      datum['USER_DEPARTMENT'] = "Computer Science"
      datum['USER_PROFILE_PIC'] = random.randint(0, 3)
    pass
  return {'data' : data}